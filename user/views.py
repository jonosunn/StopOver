from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from user.forms import RegisterForm


# Create your views here.
class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

    def post(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data.get('username')
                # message
                return redirect('home')
        else:
            form = RegisterForm()
        return render(request, self.template_name, {'form': form})


# class LoginPageView(TemplateView):
#     template_name = 'user/login.html'
