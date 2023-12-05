from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from ..views import custom_person_view
from ..models import Person
from django.core.exceptions import PermissionDenied


class CustomPersonViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.person = Person.objects.create(first_name='John', second_name='Doe', gender='M', owner=self.user)
        self.factory = RequestFactory()

    def test_custom_person_view_permission_denied(self):
        request = self.factory.get(reverse('custom-person-view', kwargs={'pk': self.person.pk + 1}))
        request.user = self.user

        with self.assertRaises(PermissionDenied):
            custom_person_view(request, pk=self.person.pk + 1)

    def test_custom_person_view_permission_granted(self):
        request = self.factory.get(reverse('custom-person-view', kwargs={'pk': self.person.pk}))
        request.user = self.user

        response = custom_person_view(request, pk=self.person.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn("John Doe", response.content.decode())
