from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory, RequestsClient

from taps.models import Tap

def create_new_tap(
    provided_title="A new Title",
    provided_author=1,
    provided_url="",
    provided_url_label="URL Label",
    provided_description="The extended description"):

    return Tap.objects.create(
    title=provided_title,
    author=provided_author,
    url=provided_url,
    url_label=provided_url_label,
    description=provided_description)

a_new_tap = {
    "title": "A new Title",
    "author": 1,
    "url": "",
    "url_label": "URL Label",
    "description": "The extended description"    
}

tap_list_url = '/api/v1/taps/'
a_tap_url = '/api/v1/taps/1/'


class TapTests(APITestCase):
    def test_get_tap(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/taps/', a_new_tap, format='json')
        # print('request.body: ', request.body)
        # # request.body:  b'{"title":"A new Title","author":1,"url":"","url_label":"URL Label","description":"The extended description"}'

        self.client = APIClient()

        # print('client: ', client)
        # # client:  <rest_framework.test.APIClient object at 0x000001ED166677C0>

        response = self.client.post('/api/v1/taps/', a_new_tap, format='json')

        # print('response', response)
        # # response <Response status_code=400, "application/json">

        # NOTE: Probably need to create user first.
        # NOTE: Probably need csrf validation with session.
        # print('response.data', response.data)
        # # response.data {'author': [ErrorDetail(string='Invalid pk "1" - object does not exist.', code='does_not_exist')]}

        response = self.client.get(tap_list_url)
        # print(response)
        # # <Response status_code=200, "application/json">
        # print(response.data)
        # # []

        response = self.client.get(a_tap_url)
        # print(response)
        # # <Response status_code=404, "application/json">
        # print(response.data)
        # # {'detail': ErrorDetail(string='Not found.', code='not_found')}


        # client = RequestsClient()
        # response = client.get(tap_list_url)
        # print(response)

        # response = self.client.get(reverse('short:index'))
        # self.assertEqual(response.status_code, 200)

        # print(reverse('api:taps'))

    # def test_create_tap(self):
    #     """
    #     Able to create a new TAP.
    #     """
    #     the_new_tap = create_new_tap()
    #     print(the_new_tap)
    #     # url = reverse('taps')
    #     url = '/api/v1/taps/'
    #     print(url)
    #     data = {
    #         "title": "A new Title",
    #         "author": 1,
    #         "url": "",
    #         "url_label": "URL Label",
    #         "description": "The extended description"            
    #     }
    #     response = self.client.post(url, data, format='json')
    #     print(response.headers)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

