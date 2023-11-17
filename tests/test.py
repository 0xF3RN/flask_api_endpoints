import unittest
import requests
import json

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url_post = "http://127.0.0.1:5000/api/v2/add/data"
        self.url_get =  "http://127.0.0.1:5000/api/v2/get/data"
        
    def test_api_add_data_x1(self):
        with open("valid_json.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 200)

    def test_api_add_data_x2(self):
        with open("valid_json_x2.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 200)
            
    def test_api_add_data_empty_fields(self):
        with open("not_valid_json_empty_fields.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 400)
            
    def test_api_add_data_no_items_field(self):
        with open("not_valid_json_no_items_field.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 400)

    def test_api_add_data_bad_hash(self):
        with open("not_valid_hash.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 400)  
    
    def test_api_get_without_params(self):
        response = requests.get(self.url_get)
        self.assertEqual(response.status_code, 200)
        
    def test_api_get_with_params(self):
        params = {
        "malwareList": ["Lockbit"]
        }
        response = requests.get(self.url_get, params=params)
        self.assertEqual(response.status_code, 200)
        
    def test_api_get_with_id_params(self):
        params = {
        "domain": "fake-fakesop.net"
        }
        response = requests.get(self.url_get, params=params)
        self.assertEqual(response.status_code, 200)        
        
    def test_api_add_data_bad_time(self):
        with open("not_valid_json_time.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 400)  

    def test_api_add_data_bad_domain(self):
        with open("not_valid_json_domain.json", "r") as file:
            send_data = json.load(file)
            response = requests.post(self.url_post, json=send_data)
            self.assertEqual(response.status_code, 400)  
    

if __name__ == "__main__":
    unittest.main()
