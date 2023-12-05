from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Person, Position


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='User_B', password='password123')
        Person.objects.create(first_name='Jan', second_name='Piekarski', gender='M', owner=user)
        Person.objects.create(first_name='Dzban', second_name='Trąbalski', gender='O', owner=user)

    def test_person_id_generation(self):
        jan = Person.objects.get(first_name='Jan')
        dzban = Person.objects.get(first_name='Dzban')
        self.assertNotEqual(jan.pk, dzban.pk)

class PositionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Position.objects.create(name='Manager', description='Responsible for team management')
        Position.objects.create(name='Developer', description='Responsible for software development')

    def test_position_id_generation(self):
        manager = Position.objects.get(name='Manager')
        developer = Position.objects.get(name='Developer')
        self.assertNotEqual(manager.pk, developer.pk)