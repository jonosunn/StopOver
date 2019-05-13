# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Account
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from user.forms import AccountForm, UserForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView

class UserDashPage(TemplateView):
    template_name = 'user/userdash.html'

    # def get(self, request, user_id):
    #     set_user = Acount.objects.get(user_id=user_id)
    #
    #
    #     args = {
    #         "user": set_user,
    #     }
    #     return render(request, self.template_name, args)

class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

    def post(self, request):

        if request.method == 'POST':
            print("Post")

            account_form = AccountForm(request.POST)
            user_form = UserForm(request.POST)

            if account_form.is_valid() and user_form.is_valid():

                # user = user_form.save()
                user = user_form.save(commit=False)
                user.username = user.email
                user.save()

                account = account_form.save(commit=False) # Don't save to the database right away

                account.user = user
                account.save()

                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password1')

                # new_user = authenticate(username=username, password=password)
                print("Account Saved")
                # message
                return redirect(reverse('login')) # Redirect to login for user to log in.

            else:
                print(account_form.is_valid())
                print(user_form.is_valid())
                print("Not Valid")
        else:
            account_form = AccountForm()
            user_form = UserForm()
            print("Account Not Saved")

        args = {
            'account_form': account_form,
            'user_form': user_form,
        }
        return render(request, self.template_name, args)

    def get(self, request):
        print("Set form")
        if request.user.is_authenticated == False: # if user is not login
            if request.method == 'GET':
                user_form = UserForm()
                account_form =AccountForm()
                args = {
                    'account_form': account_form,
                    'user_form': user_form,
                }
            return render(request, self.template_name, args)
        else:
            return redirect(reverse('home'))

class LoginPageView(LoginView):
    authentication_form = CustomAuthenticationForm
