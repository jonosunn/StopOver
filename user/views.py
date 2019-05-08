from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Account
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.urls import reverse


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
