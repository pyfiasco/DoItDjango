# pages/tests.py

from django.test import SimpleTestCase
from django.test import TestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):                     # db 미사용시 사용
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
