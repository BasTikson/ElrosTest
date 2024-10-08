from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Login(ObtainAuthToken):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            if not user.is_active:
                return Response({
                    'success': False,
                    'error': 'Пользователь не зарегистрирован или отключен.'
                }, status=status.HTTP_401_UNAUTHORIZED)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'success': True,
                'token': token.key,
                'user_id': user.pk,
            })
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class Menu(LoginRequiredMixin, TemplateView):
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        return context
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

