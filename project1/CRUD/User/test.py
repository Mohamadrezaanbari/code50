from django.urls import reverse
from django.test import TestCase, Client
from .models import User

class UserDetailViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(uid=1, firstName='mohamadreza', lastName='anbari', age=23, profession=' python & Django web programing', Address='malayer kh saadi')

    def test_userdetailview_get(self):
        response = self.client.get(reverse('userdetail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRUD/input.html')

    def test_userdetailview_post_valid_form(self):
        data = {'user_ids': '1'}
        response = self.client.post(reverse('userdetail'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRUD/details.html')
        self.assertIn('users', response.context)
        users = response.context['users']
        self.assertEqual(users.count(), 1)
        self.assertEqual(users.first().firstName, 'mohamadreza')

    def test_userdetailview_post_invalid_form(self):
        data = {'user_ids': 'invalid_id'}
        response = self.client.post(reverse('userdetail'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRUD/input.html')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertTrue(form.errors)

    def test_userdetailview_post_empty_form(self):
        response = self.client.post(reverse('userdetail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRUD/input.html')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertFalse(form.is_bound)

    def test_userdetailview_invalid_method(self):
        response = self.client.put(reverse('userdetail'))
        self.assertEqual(response.status_code, 405)

    def test_updateview_reverse(self):
        url = reverse('update', args=[self.user.uid])
        self.assertEqual(url, f'/{self.user.uid}/')

    def test_deleteview_reverse(self):
        url = reverse('delete', args=[self.user.uid])
        self.assertEqual(url, f'/delete/{self.user.uid}')
