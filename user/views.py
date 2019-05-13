# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from user.forms import AccountForm, UserForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from booking.models import Booking
import datetime
import stripe
from django.contrib import messages

class UserDashPage(TemplateView):
	template_name = 'user/userdash.html'

	def get(self, request):

		user = request.user

		# Get the current user logged in and their current booking
		# if user.account.book_status == True:
		curr_booking = Booking.objects.all().filter(user_id=user.id).order_by("-id")[0]

		# Get the booking history
		booking_history = None
			
		if user.account.book_status == True:
			print("True")
			booking_history = Booking.objects.all().filter(user_id=user.id).order_by("-id")[1:]
		else:
			booking_history = Booking.objects.all().filter(user_id=user.id)

		args = {
			"booking": curr_booking,
			"booking_history": booking_history
		}

		return render(request, self.template_name, args)

	def post(self, request):

		if request.method == 'POST':

			# Get current user's booking
			user = request.user
			curr_booking = Booking.objects.all().filter(user_id=user.id).order_by("-id")[0]

			# Get and save booking end date and time to booking model
			curr_booking.end_date = datetime.date.today()
			curr_booking.end_time = datetime.datetime.now().time()
			curr_booking.save()

			# Calculate price for booking
			start = datetime.datetime.combine(curr_booking.start_date, curr_booking.start_time)
			end = datetime.datetime.combine(curr_booking.end_date, curr_booking.end_time)
			time_difference = end - start
			seconds = time_difference.total_seconds()

			# Determine hours and minutes rounded with 2 decimal places
			duration = round((seconds/60/60), 2)

			# Determine price subtracting initial $10 booking deposit fee and round to nearest dollar
			price_in_dollars = int(round((duration * curr_booking.price) - 10))
			
			# Convert to cents for stripe format
			price_in_cents = price_in_dollars * 100

			# Save actual price paid to database
			curr_booking.actual_price = price_in_dollars + 10
			curr_booking.save()

			# Charge the Customer instead of the card:
			charge = stripe.Charge.create(
				amount=price_in_cents,
				currency='aud',
				customer=curr_booking.customer_id,
			)

			return render(request, "user/return_success.html")

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


class LoginPageView(LoginView):
    authentication_form = CustomAuthenticationForm