# Project Documentation: Flask Server
## Introduction

Welcome to the documentation for my project, which includes a Flask sever and a parser (extra: test client). This documentation will guide you through the installation and usage of the project components.

## Installation

To get started with the project, follow these installation steps:

1) Clone the repository:

```bash
git clone https://github.com/cutecei/flask_api_endpoints.git
```

2) Navigate to the project directory:

```bash
cd flask_api_endpoints
```

3) Install the project dependencies:
```bash
pip install -r requirements.txt
```

4) Run MongoDB server
   Make sure you have created facct collection

6) Run server
```bash
python flask_server.py
```

## Usage

This project has method: POST and GET

1) POST:
   
   Allows the client to add data to MongoDB. Also there is a parser that checks the data to see if it matches the required format and if the fields are not empty.
```python
   def send_json(json_file):
    with open(json_file, "r") as file:
        send_data = json.load(file)
        response = requests.post(url_post, json=send_data)
        print(response.text)
```

2) GET:
   
   Allows the client to retrieve data from MongoDB. Also client can add params for advanced search.
```python
def get_data():
    params = {
        "malwareList": ["Lockbit"]
    }
    response = requests.get(url_get, params=params)
    print(response.json())
```
or
```python
def get_data():
    params = {
        "dateFirstSeen": "2023-09-30T11:03:52+00:00",
        "dateLastSeen": "2023-09-30T11:03:52+00:00"
    }
    response = requests.get(url_get, params=params)
    print(response.json())
```
