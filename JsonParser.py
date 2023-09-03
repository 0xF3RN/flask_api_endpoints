import sys


class JSONParser:
    def __init__(self, json_data):
        self.data = json_data
        sys.setrecursionlimit(2000)
        print(f"-> parser has been initialized, recursion limit is {sys.getrecursionlimit()}")

    def __del__(self):
        print("-> parser has been deleted")

    def json_validation(self, data=None):
        if data is None:
            data = self.data
        if isinstance(data, dict):
            if not data:
                return False
            for key, value in data.items():
                if value is None or (isinstance(value, str) and value.strip() == ""):
                    return False
                elif isinstance(value, (dict, list)):
                    if not self.json_validation(value):
                        return False
        elif isinstance(data, list):
            if not data:
                return False
            for item in data:
                if not self.json_validation(item):
                    return False
        return True
