from util.api import GoogleMapsAPI
from util.httpmethods import HttpMethods


class TestCreatePlace():
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()
        json_result = result_post.json()
        place_id = json_result['place_id']

        print('Метод GET - POST')
        result_get = GoogleMapsAPI.get_new_place(place_id)

        print('Метод PUT')
        result_put = GoogleMapsAPI.put_new_place(place_id)
        
        print('Метод GET - PUT')
        result_get = GoogleMapsAPI.get_new_place(place_id)

        print('Метод DELETE')
        result_del = GoogleMapsAPI.del_new_place(place_id)
        
        print('Метод GET - DELETE')
        result_get = GoogleMapsAPI.get_new_place(place_id)

        