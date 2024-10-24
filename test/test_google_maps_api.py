from util.api import GoogleMapsAPI


class TestCreatePlace():
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()