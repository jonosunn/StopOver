from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views
from .models import Car

class MapAppTest(TestCase):
    # Test for database models
    # Set up dummy car object
    def setUp(self):
        Car.objects.create(brand='test_brand', transmission='automatic', number_plate='TEST01',
            price=100, longitude=-37.6799703, latitude=145.0548504, available=True, colour='Blue',
            seat_no=5, year=2020)

    # Test for content within created dummy object
    def test_car_content(self):
        car = Car.objects.get(id=1)
        expected_object_brand = car.brand
        expected_object_transmission = car.transmission
        expected_object_number_plate = car.number_plate
        expected_object_price = car.price
        expected_object_longitude = car.longitude
        expected_object_latitude = car.latitude
        expected_object_available = car.available
        expected_object_colour = car.colour
        expected_object_seat_no = car.seat_no
        expected_object_year = car.year
        self.assertEquals(expected_object_brand, 'test_brand')
        self.assertEquals(expected_object_transmission, 'automatic')
        self.assertEquals(expected_object_number_plate, 'TEST01')
        self.assertEquals(expected_object_price, 100)
        self.assertEquals(expected_object_longitude, -37.6799703)
        self.assertEquals(expected_object_latitude, 145.0548504)
        self.assertTrue(expected_object_available, True)
        self.assertEquals(expected_object_brand, 'Blue')
        self.assertEquals(expected_object_seat_no, 5)
        self.assertEquals(expected_object_year, 2020)

    # Test data types of car object
    def test_data_type(self):
        car = Car.objects.get(id=1)
        self.assertIsInstance(car.brand, str)
        self.assertIsInstance(car.transmission, str)
        self.assertIsInstance(car.number_plate, str)
        self.assertIsInstance(car.price, int)
        self.assertIsInstance(car.longitude, float)
        self.assertIsInstance(car.latitude, float)
        self.assertIsInstance(car.available, bool)


    # Test for correct web application routing
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'map/homepage.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('')
        self.assertContains(response, '<title>Homepage</title>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
