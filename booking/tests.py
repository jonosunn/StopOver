from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views
from map.models import Car
from django.contrib.auth.models import User

class MapAppTest(TestCase):
    # Test for database models
    # Set up dummy car object
    def setUp(self):
        Car.objects.create(brand='test_brand', transmission='automatic', number_plate='TEST01',
            price=100, longitude=-37.6799703, latitude=145.0548504, available=True)

        self.user = User.objects.create(username="teststop")
        self.user.set_password("whatisthepassword")
        self.user.save()

    def test_booking_page_status_code(self):
        self.client.force_login(self.user)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)

    def test_booking_url_by_name(self):
        self.client.force_login(self.user)
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)

    def test_booking_uses_correct_template(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')

    def test_booking_page_contains_correct_html(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertContains(response, '<title>Booking</title>')

    def test_booking_page_does_not_contain_incorrect_html(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('booking', args=(car.number_plate,)))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_confirmation_page_status_code(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('confirmation'))
        self.assertEquals(response.status_code, 200)

    def test_confirmation_url_by_name(self):
        car = Car.objects.get(id=1)
        response = self.client.get(reverse('confirmation'))
        self.assertEquals(response.status_code, 200)

    def test_confirmation_uses_correct_template(self):
        response = self.client.get(reverse('confirmation'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/confirmation.html')

    def test_confirmation_page_contains_correct_html(self):
        response = self.client.get(reverse('confirmation'))
        self.assertContains(response, '<title>Confirmation</title>')

    def test_confirmation_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('confirmation'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_success_page_status_code(self):
        response = self.client.get(reverse('success'))
        self.assertEquals(response.status_code, 200)

    def test_success_url_by_name(self):
        response = self.client.get(reverse('success'))
        self.assertEquals(response.status_code, 200)

    def test_success_uses_correct_template(self):
        response = self.client.get(reverse('success'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/success.html')

    def test_success_page_contains_correct_html(self):
        response = self.client.get(reverse('success'))
        self.assertContains(response, '<title>Success</title>')

    def test_success_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('success'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
