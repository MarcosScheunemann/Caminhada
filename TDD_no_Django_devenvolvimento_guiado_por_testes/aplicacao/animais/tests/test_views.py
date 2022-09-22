from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'lagarto',
            predador = 'Sim',
            venenoso = 'Sim',
            domestico = 'Não',
        )

    def test_index_view_retorna_caracteristicas_do_animal(self):
        response = self.client.get('/', 
            {'buscar':'lagarto'}
        )
        caracteristica_animal = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal[0].nome_animal, 'lagarto')
