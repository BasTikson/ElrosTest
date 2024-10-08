from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.authtoken.models import Token

class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/') and not request.path.startswith('/api/token/'):
            if 'HTTP_AUTHORIZATION' not in request.META:
                return redirect(reverse('login'))
            auth_header = request.META['HTTP_AUTHORIZATION']
            if not auth_header.startswith('Token '):
                return redirect(reverse('login'))
            token_key = auth_header.split(' ')[1]
            try:
                token = Token.objects.get(key=token_key)
                request.user = token.user
            except Token.DoesNotExist:
                return redirect(reverse('login'))

        response = self.get_response(request)
        return response