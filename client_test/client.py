import requests
import json

url1 = "http://127.0.0.1:5000/api/add"
url = 'http://127.0.0.1:5000/api/get'

def send_json(json_file):
    with open(json_file, "r") as file:
        send_data = json.load(file)
        response = requests.post(url1, json=send_data)
        print(response.text)


def get_data():
    response = requests.get(url)
    print(response.json())


def main():
    get_data()
    #send_json("valid_json.json")
    #send_json("valid_json_x2.json")
    #send_json("not_valid_json_no_items_field.json")     # without items field
    #("not_valid_json_empty_fields.json")                # empty fields

if __name__ == "__main__":
    main()
