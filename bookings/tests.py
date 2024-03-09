from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class LoginTestCase(TestCase):
    def setUp(self):
        # Creates a test user for all tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # Tests if the login page loads successfully
    def test_loginpage(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Tests if the user can log in with valid credentials and is redirected to the correct page
    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('book_table'))

    # Tests if the website will disallow a user from logging in when entering invalid login credentials, and if the user can still see the login page when they enter invalid

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'notvaliduser', 'password': 'notvalidpassword'})
        self.assertEqual(response.status_code, 200)


