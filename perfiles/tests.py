from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from perfiles.forms import UserRegisterForm

class TestdeVistaDeRegistros(TestCase):
    def test_registro_exitoso(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
        }
        response = self.client.post(reverse('registro'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_registro_fallido(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'TestCotranseñaErronea',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
        }
        response = self.client.post(reverse('registro'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())

