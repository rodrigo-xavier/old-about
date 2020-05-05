from django.test import TestCase
from utils.models import PhoneField
from unittest import mock
import pytest


class PhoneFieldTestCase(TestCase):
    def setUp(self):
        PhoneField.objects.create(phone=9999)
        PhoneField.objects.create(phone=999999999)
        PhoneField.objects.create(phone=000000000)
        PhoneField.objects.create(phone=999999999999999)
        # PhoneField.objects.create(phone=+00000000000000)
    
    def test_validate_phone(self):
        phone = PhoneField.objects.all()

        assert phone[0].phone == '9999'
        assert phone[1].phone == '999999999'
        assert phone[2].phone == '0'
        assert phone[3].phone == '999999999999999'
        # assert phone[4].phone != 9999999999999999
        
    # def tearDown(self):
    #     PhoneField.objects.get.all().delete()
    #     return super().tearDown()