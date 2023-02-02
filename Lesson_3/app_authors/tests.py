from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import AuthorModel, BiographyModel

# Create your tests here.
class TestAuthorViewSet(TestCase):
    

    def setUp(self) -> None:
        self.name = 'Admin'
        self.password = 'admin123_%#$'

        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Александро', 'last_name': 'Пушко', 'birthday_year': 1900}
        self.url = '/api/authors_router/'
        self.admin = User.objects.create_superuser(self.name, 'admin@email.ru', self.password)
        #return super().setUp()

    def test_get_list(self):
        #Создаём объект класса APIRequestFactory
        factory = APIRequestFactory()
        #Определяем адрес и метод для отправки запроса
        request = factory.get(self.url)
        #Указываем какой тип запроса будет передан в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'get':'list'})
        #Передаём во view и получаем ответ
        response = view(request)
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_guest(self):
        #Создаём объект класса APIRequestFactory
        factory = APIRequestFactory()
        #Определяем адрес и метод для отправки запроса
        request = factory.post(self.url, self.data, format='json')
        #Указываем какой тип запроса будет передан в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'post':'create'})
        #Передаём во view и получаем ответ
        response = view(request)
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_create_admin(self):
        #Создаём объект класса APIRequestFactory
        factory = APIRequestFactory()
        #Определяем адрес и метод для отправки запроса
        request = factory.post(self.url, self.data, format='json')
        #Авторизоваться
        force_authenticate(request, self.admin)
        #Указываем какой тип запроса будет передан в AuthorModelViewSet
        view = AuthorModelViewSet.as_view({'post':'create'})
        #Передаём во view и получаем ответ
        response = view(request)
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_detail(self):
        #Создаём объект класса APIClient
        client = APIClient()
        #Создать автора через ORM для проверки детализации
        author = AuthorModel.objects.create(**self.data)
        #Сделать запрос
        response = client.get(f'{self.url}{author.id}/')
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_guest(self):
        #Создаём объект класса APIClient
        client = APIClient()
        #Создать автора через ORM для проверки обновления
        author = AuthorModel.objects.create(**self.data_put)
        #Сделать запрос на обновление
        response = client.put(f'{self.url}{author.id}/', self.data_put)
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_admin(self):
        #Создаём объект класса APIClient
        client = APIClient()
        #Создать автора через ORM для проверки обновления
        author = AuthorModel.objects.create(**self.data_put)
        #Авторизуемся
        client.login(username=self.name, password=self.password)
        #Сделать запрос на обновление
        response = client.put(f'{self.url}{author.id}/', self.data_put)
        #Проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Получаем автора
        author_update = AuthorModel.objects.get(id=author.id)
        #Делаем проверку
        self.assertEqual(author_update.first_name, 'Александро')
        self.assertEqual(author_update.last_name, 'Пушко')
        self.assertEqual(author_update.birthday_year, 1900)
        client.logout()


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response, 2)

class TestBiographyViewSet(APITestCase):
    def setUp(self) -> None:
        self.name = 'Admin'
        self.password = 'admin123_%#$'

        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Александро', 'last_name': 'Пушко', 'birthday_year': 1900}
        self.url = '/api/biography_router/'
        self.admin = User.objects.create_superuser(self.name, 'admin@email.ru', self.password)

    def test_get_list(self):
        #Делаем запрос
        response = self.client.get(self.url)
        #Проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        #Создать автора через ORM для связи с биографией
        author = AuthorModel.objects.create(**self.data)
        #Создать боиграфию
        bio = BiographyModel.objects.create(text='test', author=author)
        #Авторизация
        self.client.login(username=self.name, password=self.password)
        #Запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text':'Biography','author':bio.author.id})
        #Проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Получаем биографию
        biog = BiographyModel.objects.get(id=bio.id)
        #Сделать проверку
        self.assertEqual(biog.text, 'Biography')
        #Выходим
        self.client.logout()

    def test_edit_mixer(self):
        #Создать автора через ORM для связи с биографией
        #author = AuthorModel.objects.create(**self.data)
        #Создать боиграфию
        bio = mixer.blend(BiographyModel)
        #Авторизация
        self.client.login(username=self.name, password=self.password)
        #Запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text':'Biography','author':bio.author.id})
        #Проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Получаем биографию
        biog = BiographyModel.objects.get(id=bio.id)
        #Сделать проверку
        self.assertEqual(biog.text, 'Biography')
        #Выходим
        self.client.logout()

    
    def test_edit_mixer_text(self):
        #Создать автора через ORM для связи с биографией
        #author = AuthorModel.objects.create(**self.data)
        #Создать боиграфию
        bio = mixer.blend(BiographyModel, text='Вася')
        #Авторизация
        self.client.login(username=self.name, password=self.password)
        #Запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text':'Biography','author':bio.author.id})
        #Проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #Получаем биографию
        biog = BiographyModel.objects.get(id=bio.id)
        #Сделать проверку
        self.assertEqual(biog.text, 'Biography')
        #Выходим
        self.client.logout()