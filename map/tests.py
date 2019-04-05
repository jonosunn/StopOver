from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views

class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status.code, 200)
