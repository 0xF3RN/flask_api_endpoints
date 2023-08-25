import requests
import json

url_post = "http://127.0.0.1:5000/api/v2/add/data"
url_get = "http://127.0.0.1:5000/api/v2/get/data"


def send_json(json_file):
    with open(json_file, "r") as file:
        send_data = json.load(file)
        response = requests.post(url_post, json=send_data)
        print(response.text)


def get_data():
    params = {
        "malwareList": ["Lockbit"]
    }
    response = requests.get(url_get, params=params)
    print(response.json())


def main():
    get_data()                                           # gets data based on params
    #send_json("valid_json.json")                        # adds 1 json
    #send_json("valid_json_x2.json")                     # adds 2 jsons
    #send_json("not_valid_json_no_items_field.json")     # without items field
    #send_json("not_valid_json_empty_fields.json")       # empty fields


if __name__ == "__main__":
    main()
