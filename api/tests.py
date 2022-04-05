from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory, RequestsClient

from taps.models import Tap
from users.models import CustomUser

a_test_user = {
    "username": 'Dezzi',
    "email": 'dezzi@thekitten.edu',
    "password": '1234fuzzy',
}

a_second_test_user = {
    "username": 'HarleyQuinn',
    "email": 'harley@quinn.gov',
    "password": '1234test'
}

a_test_tap = {
    "title": "A new Title",
    "author": 1,
    "url": "",
    "url_label": "URL Label",
    "description": "The extended description"    
}

taps_endpoint = '/api/v1/taps/'

users_endpoint = '/api/v1/users/'


# TODO: Does this create a user in the test database when called in test function?
def create_test_user(
    provided_username='HarleyQuinn',
    provided_email='harley@quinn.gov',
    provided_password='1234test'):

    return CustomUser.objects.create(
            username = provided_username,
            email = provided_email,
            password = provided_password 
    )

def create_a_second_test_user(
    provided_username='JessicaJones',
    provided_email='jessica@jones.gov',
    provided_password='test1234'):

    return CustomUser.objects.create(
            username = provided_username,
            email = provided_email,
            password = provided_password 
    )

class TestUsersAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        a_test_user = {
            "username": 'Dezzi',
            "email": 'dezzi@thekitten.edu',
            "password": '1234fuzzy',
        }
        a_second_test_user = {
            "username": 'HarleyQuinn',
            "email": 'harley@quinn.gov',
            "password": '1234test'
        }
        a_test_tap = {
            "title": "A new Title",
            "author": 1,
            "url": "",
            "url_label": "URL Label",
            "description": "The extended description"    
        }
        taps_endpoint = '/api/v1/taps/'
        users_endpoint = '/api/v1/users/'


    def test_create_user(self):
        """
        Database should contain zero records when there are not users and then one record after user is added.
        """
        self.assertEqual(CustomUser.objects.count(), 0)
        
        response = self.client.post(users_endpoint, a_test_user, format='json')
        self.assertEqual(CustomUser.objects.count(), 1)


    def test_retrieve_user(self):
        """
        Call to users endpoint should return the user in the database. This instance attributes should match the ones provided when user is created.
        """
        response = self.client.post(users_endpoint, a_test_user, format='json')
        
        response = self.client.get(users_endpoint)
        self.assertEqual(response.data[0]['username'], a_test_user['username'])
        self.assertEqual(response.data[0]['email'], a_test_user['email'])


        # # These are responses from the database.
        # self.assertEqual(CustomUser.objects.get().username, a_test_user['username'])
        # self.assertEqual(CustomUser.objects.get().email, a_test_user['email'])

    # def test_retrieve_user(self):

    #     self.assertEqual(CustomUser.objects.count(), 0)
    #     response = self.client.post(users_endpoint, a_test_user, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(CustomUser.objects.count(), 1)
    #     self.assertEqual(CustomUser.objects.get().username, 'Dezzi')
    #     self.assertEqual(CustomUser.objects.get().email, 'dezzi@thekitten.edu')

    #     response = self.client.post(users_endpoint, a_second_test_user, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     response = self.client.get(users_endpoint)
    #     self.assertEqual(CustomUser.objects.count(), 2)
        
        # print('response.data: ', response.data)     # response.data:  {'id': 1, 'username': 'Dezzi', 'taps_detail': []}
        # response = self.client.get(users_endpoint)
        # print('response.data: ', response.data)     # response.data:  [OrderedDict([('id', 1), ('username', 'Dezzi'), ('taps_detail', [])])]
        # print('response.data[0]: ', response.data[0])  # response.data:  OrderedDict([('id', 1), ('username', 'Dezzi'), ('taps_detail', [])])
        # print('response.data[0].keys(): ', response.data[0].keys()) # response.data:  odict_keys(['id', 'username', 'email', 'taps_detail'])
        # print("response.data[0]['id']: ", response.data[0]['id'])   # response.data[0]['id']:  1
        # print("response.data[0]['username']: ", response.data[0]['username'])   # response.data[0]['username']:  Dezzi
        # print('len(response.data)', len(response.data)) # len(response.data) 1


        


class TestTapsAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        a_test_user = {
            "username": 'Dezzi',
            "email": 'dezzi@thekitten.edu',
            "password": '1234fuzzy',
        }
        a_second_test_user = {
            "username": 'HarleyQuinn',
            "email": 'harley@quinn.gov',
            "password": '1234test'
        }
        a_test_tap = {
            "title": "A new Title",
            "author": 1,
            "url": "",
            "url_label": "URL Label",
            "description": "The extended description"    
        }
        taps_endpoint = '/api/v1/taps/'
        users_endpoint = '/api/v1/users/'

    def test_create_tap(self):
        """
        Database should contain zero records when there are no taps and then one record after one tap is added.
        """
        self.assertEqual(Tap.objects.count(), 0)
        the_first_user = create_test_user()
        a_test_tap['author'] = the_first_user.id
        
        response = self.client.post(taps_endpoint, a_test_tap, format='json')
        self.assertEqual(Tap.objects.count(), 1)



    def test_retrieve_tap(self):
        """
        Call to taps endpoint should return the tap in the database. This instance attributes should match the ones provided when tap is created.
        """
        the_first_user = create_test_user()
        a_test_tap['author'] = the_first_user.id
        response = self.client.post(taps_endpoint, a_test_tap, format='json')
        
        response = self.client.get(taps_endpoint)
        self.assertEqual(response.data[0]['title'], a_test_tap['title'])
        self.assertEqual(response.data[0]['author'], a_test_tap['author'])        
        self.assertEqual(response.data[0]['url'], a_test_tap['url'])        
        self.assertEqual(response.data[0]['url_label'], a_test_tap['url_label'])        
        self.assertEqual(response.data[0]['description'], a_test_tap['description'])        

        # print('response.data: ', response.data)
        # response.data:  {'id': 1, 'title': 'A new Title', 'author': 1, 'author_detail': OrderedDict([('id', 1), ('username', 'HarleyQuinn')]), 'url': '', 'url_label': 'URL Label', 'description': 'The extended description'}

