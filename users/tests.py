from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from .permissions import IsDoctor, IsAdministrator, IsAdminOrDoctor
# Create your tests here.

User = get_user_model()


class TestMedicalPermissions(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.perm_doctor = IsDoctor()
        self.perm_admin = IsAdministrator()
        self.perm_admin_or_doctor = IsAdminOrDoctor()

        self.view = object()

        # Har bir user uchun noyob telefon raqam
        self.doctor_user = User.objects.create_user(
            username='doc',
            role='shifokor',
            phone_number='+998901234567'
        )
        self.admin_user = User.objects.create_user(
            username='adm',
            role='admin',
            phone_number='+998907654321'
        )
        self.anon_user = AnonymousUser()

    def _get_request(self, user):
        request = self.factory.get('/fake-url/')
        request.user = user
        return request

    # IsDoctor uchun testlar
    def test_is_doctor_allows_doctor(self):
        req = self._get_request(self.doctor_user)
        self.assertTrue(self.perm_doctor.has_permission(req, self.view))

    def test_is_doctor_denies_admin_and_others(self):
        req_admin = self._get_request(self.admin_user)
        req_anon = self._get_request(self.anon_user)
        self.assertFalse(self.perm_doctor.has_permission(req_admin, self.view))
        self.assertFalse(self.perm_doctor.has_permission(req_anon, self.view))

    # IsAdminOrDoctor uchun testlar
    def test_admin_or_doctor_allows_both(self):
        req_doc = self._get_request(self.doctor_user)
        req_admin = self._get_request(self.admin_user)
        self.assertTrue(self.perm_admin_or_doctor.has_permission(req_doc, self.view))
        self.assertTrue(self.perm_admin_or_doctor.has_permission(req_admin, self.view))

    def test_admin_or_doctor_denies_other_roles_and_anon(self):
        req_anon = self._get_request(self.anon_user)
        self.assertFalse(self.perm_admin_or_doctor.has_permission(req_anon, self.view))

