from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from . import views
from map.models import Car
from booking.models import Booking
from django.contrib.auth.models import User
import datetime

class BookingAppTest(TestCase):
    # Test for database models
    # Set up dummy car object
    def setUp(self):
        booked_car = Car.objects.create(brand='test_brand', transmission='automatic', number_plate='TEST01',
            price=100, longitude=-37.6799703, latitude=145.0548504, available=True, colour='Blue', seat_no=5,
            year=2020)

        self.testuser = User.objects.create(username="teststop@email.com")
        self.testuser.set_password("whatisthepassword")
        self.testuser.save()

        # Initialize booking
        booking = Booking.objects.create(brand=booked_car.brand, transmission=booked_car.transmission, number_plate=booked_car.number_plate,
                                        price=booked_car.price, start_latitude=booked_car.latitude, start_longitude=booked_car.longitude, user=self.testuser)
        booking.end_date = datetime.date.today()
        booking.end_time = datetime.datetime.now().time()

        # Assume user booked for 2 hours
        booking.actual_price = 2 * booking.price

        # Add customer id
        booking.customer_id = "test_customerID"
        booking.save()


    def test_booking_page_status_code(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)

    def test_booking_url_by_name(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)

    def test_booking_uses_correct_template(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')

    def test_booking_page_contains_correct_html(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertContains(response, '<title>Booking</title>')

    def test_booking_page_does_not_contain_incorrect_html(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    # Testing redirect to login
    def test_booking_login_redirect(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 302)

    def test_confirmation_page_status_code(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.post(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertEquals(response.status_code, 200)

    def test_confirmation_url_by_name(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.post(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertEquals(response.status_code, 200)

    def test_confirmation_uses_correct_template(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.post(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/confirmation.html')

    def test_confirmation_page_contains_correct_html(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.post(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertContains(response, '<title>Confirmation</title>')

    def test_confirmation_page_does_not_contain_incorrect_html(self):
        self.client.force_login(self.testuser)
        car = Car.objects.get(id=1)
        response = self.client.post(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    # Test redirect to home.
    def test_confirmation_home_redirect(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('confirmation'), {'number_plate':car.number_plate})
        self.assertEquals(response.status_code, 302)

    def test_success_page_status_code(self):
        self.client.force_login(self.testuser)
        response = self.client.post(reverse('success'))
        self.assertEquals(response.status_code, 200)

    def test_success_url_by_name(self):
        self.client.force_login(self.testuser)
        response = self.client.post(reverse('success'))
        self.assertEquals(response.status_code, 200)

    def test_success_uses_correct_template(self):
        self.client.force_login(self.testuser)
        response = self.client.post(reverse('success'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/success.html')

    def test_success_page_contains_correct_html(self):
        self.client.force_login(self.testuser)
        response = self.client.post(reverse('success'))
        self.assertContains(response, '<title>Success</title>')

    def test_success_page_does_not_contain_incorrect_html(self):
        self.client.force_login(self.testuser)
        response = self.client.post(reverse('success'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    # Testing redirect to home
    def test_success_home_redirect(self):
        self.client.force_login(self.testuser)
        response = self.client.get(reverse('success'))
        self.assertEquals(response.status_code, 302)

    # Tests that content in booking is correct and has relationship with the user
    def test_booking_content(self):
        booking = Booking.objects.get(user_id=self.testuser.id)
        expected_brand = booking.brand
        expected_transmission = booking.transmission
        expected_number_plate = booking.number_plate
        expected_price = booking.price
        expected_latitude = booking.start_latitude
        expected_longitude = booking.start_longitude
        epxected_actual_price = booking.actual_price
        expected_end_date = booking.end_date
        expected_end_time = booking.end_time
        expected_customer_id = booking.customer_id

        self.assertEquals(expected_brand, 'test_brand')
        self.assertEquals(expected_transmission, 'automatic')
        self.assertEquals(expected_number_plate, 'TEST01')
        self.assertEquals(expected_price, 100)
        self.assertEquals(expected_latitude, 145.0548504)
        self.assertEquals(expected_longitude, -37.6799703)
        self.assertEquals(epxected_actual_price, 200)
        self.assertIsInstance(expected_end_date, datetime.date)
        self.assertIsInstance(expected_end_time, datetime.time)
        self.assertEquals(expected_customer_id, "test_customerID")
