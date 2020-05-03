from django.test import TestCase
from utils.models import PhoneField


class PhoneFieldTestCase(TestCase):
    def setUp(self):
        self.test1 = PhoneField.objects.create(phone_number=9999)
        self.test2 = PhoneField.objects.create(phone_number=999999999)

    def test_regex(self):
        phone = PhoneField.objects.get.all()
        self.assertEqual(self.test1, )
        