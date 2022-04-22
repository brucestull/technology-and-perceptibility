# from django.urls import reverse
from urllib import response
from rest_framework import status
# from rest_framework.test import APIClient, APIRequestFactory, RequestsClient
from rest_framework.test import APITestCase

from taps.models import Tap
from users.models import CustomUser

# Command to run tests:
# python ./manage.py test

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
    "author": 1,
    "url": "",
    "url_label": "URL Label",
    "description": "The extended description"    
}

taps_endpoint = '/api/v1/taps/'

users_endpoint = '/api/v1/users/'


def create_test_user(user):
    return CustomUser.objects.create(
            username = user['username'],
            email = user['email'],
            password = user['password']
    )


class TestUsersAPINoUsers(APITestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_create_user(self):
        """
        Database should contain zero records when there are not users and then one record after user is added. That record should reflect the values of the added user.
        """
        self.assertEqual(CustomUser.objects.count(), 0)
        
        response = self.client.post(users_endpoint, a_test_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, a_test_user['username'])
        # self.assertEqual(CustomUser.objects.get().email, a_test_user['email'])


class TestUsersAPIWithUsers(APITestCase):
    @classmethod
    def setUpTestData(cls):
        the_first_user = create_test_user(a_test_user)
        a_test_tap['author'] = the_first_user.id

    def setUp(self):
        pass

    def test_retrieve_user(self):
        """
        Call to users endpoint should return the user in the database. This instance attributes should match the ones provided when user is created.
        """
        response = self.client.get(users_endpoint)
        self.assertEqual(response.data[0]['username'], a_test_user['username'])
        # self.assertEqual(response.data[0]['email'], a_test_user['email'])

    def test_delete_user(self):
        """
        Deleting user should return 204. After deletion, there should be no users in database.
        """
        self.assertEqual(CustomUser.objects.count(), 1)

        the_id = CustomUser.objects.get().id
        response = self.client.delete(f"{users_endpoint}{the_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)


class TestTapsAPI(APITestCase):
    @classmethod
    def setUpTestData(cls):
        the_first_user = create_test_user(a_test_user)
        a_test_tap['author'] = the_first_user.id

    def setUp(self):
        pass

    def test_create_tap(self):
        """
        Database should contain zero records when there are no taps and then one record after one tap is added. The values of the taps should reflect values provided in the 'post' request.
        """
        response = self.client.post(taps_endpoint, a_test_tap, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tap.objects.count(), 1)
        self.assertEqual(Tap.objects.get().url, a_test_tap['url'])
        self.assertEqual(Tap.objects.get().url_label, a_test_tap['url_label'])
        self.assertEqual(Tap.objects.get().description, a_test_tap['description'])

    def test_retrieve_tap(self):
        """
        Call to taps endpoint should return the tap in the database. This instance attributes should match the ones provided when tap is created.
        """
        response = self.client.post(taps_endpoint, a_test_tap, format='json')
        
        response = self.client.get(taps_endpoint)
        self.assertEqual(response.data[0]['author'], a_test_tap['author'])        
        self.assertEqual(response.data[0]['url'], a_test_tap['url'])        
        self.assertEqual(response.data[0]['url_label'], a_test_tap['url_label'])        
        self.assertEqual(response.data[0]['description'], a_test_tap['description'])        
