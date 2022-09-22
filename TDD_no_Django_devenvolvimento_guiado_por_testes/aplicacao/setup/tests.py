from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/Marcos/Desktop/python/pythonProject/TDD_no_Django_devenvolvimento_guiado_por_testes/aplicacao/chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'lagarto',
            predador = 'Sim',
            venenoso = 'Sim',
            domestico = 'Não',
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """       Teste se um usuário encontra um animal pesquisando
        """
        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo:leão')
        
        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        sleep(0.5)
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)
        # Ele desiste de adotar um leão.
        sleep(1)