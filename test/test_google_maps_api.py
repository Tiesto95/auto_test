from util.api import GoogleMapsAPI
from util.httpmethods import HttpMethods


class TestCreatePlace():
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()
        json_result = result_post.json()
        place_id = json_result['place_id']

        print('Метод GET')
        result_get = GoogleMapsAPI.get_new_place(place_id)

