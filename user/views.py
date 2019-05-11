from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from user.forms import AccountForm, UserForm


# Create your views here.
class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

    def post(self, request):
        if request.method == 'POST':
            print("Post")

            account_form = AccountForm(request.POST)
            user_form = UserForm(request.POST)

            if account_form.is_valid() and user_form.is_valid():

                user = user_form.save()
                account = account_form.save(commit=False) # Don't save to the database right away
                account.user = user
                account.save()

                username = user_form.cleaned_data.get('username')
                password = user_form.cleaned_data.get('password1')

                # new_user = authenticate(username=username, password=password)
                print("Account Saved")
                # message
                return redirect('login') # Redirect to login for user to log in.

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
        if request.method == 'GET':
            user_form = UserForm()
            account_form =AccountForm()
        args = {
            'account_form': account_form,
            'user_form': user_form,
        }
        return render(request, self.template_name, args)


# class LoginPageView(TemplateView):
#     template_name = 'user/login.html'
