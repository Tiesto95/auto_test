from .httpmethods import HttpMethods

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsAPI():
    @staticmethod
    def create_new_place():
        json_create_new_place = {
                "location": { 
                "lat": -38.383494, 
                "lng": 33.427362 
                }, "accuracy": 50, 
                "name": "Frontline house", 
                "phone_number": "(+91) 983 893 3937", 
                "address": "29, side layout, cohen 09", 
                "types": [
                "shoe park", 
                "shop"
                ],
                "website": "http://google.com", 
                "language": "French-IN"
                }
        post_resurce = "/maps/api/place/add/json"
        post_url = base_url + post_resurce + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        get_resurce = "/maps/api/place/get/json"
        get_url = base_url + get_resurce + key + '&place_id='+place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get
        
    @staticmethod
    def put_new_place(place_id):
        put_resurce = "/maps/api/place/update/json"
        put_url = base_url + put_resurce + key
        print(put_url)
        json_body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_body)
        print(result_put.text)
        return result_put
    