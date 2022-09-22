from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',

        )

    def test_animal_cadastrado(self):

        self.assertEqual(self.animal.nome_animal, 'leão')
