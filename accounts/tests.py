from django.test import TestCase
from . models import CustomUser


class UserTests(TestCase):
    def test_for_user_creation(self):
        user_model = CustomUser.objects.create(
          username='Tailor',
          password='somepass',
          email='Kaitin@gmail.com'
        )
        self.assertEquals(user_model.username, 'Tailor')
