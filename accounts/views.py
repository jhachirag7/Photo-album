from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldVal': request.POST,
        }
        if len(password) < 8:
            messages.error(request, 'Password too short')
            return render(request, 'accounts/register.html', context=context)
        user = User.objects.create_user(
            username=username, password=password, email=email)
        user.save()
        messages.success(
            request, "Account successfully created for activation confirm your mail from your accounts")
        return render(request, 'accounts/login.html')


class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html")
