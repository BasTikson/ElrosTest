from rest_framework.authtoken.models import Token
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

class LoginView(View):
    template_name = 'login.html'
    api_interaction_url = 'api_interaction'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return redirect(self.api_interaction_url)
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})



class ApiInteractionView(View):
    template_name = 'api_interaction.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)