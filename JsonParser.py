import json


class JSONParser:
    def __init__(self, json_data):
        self.data = json_data
        print("-> parser has been initialized")

    def print_data(self):
        return self.data    # for debug

    def __del__(self):
        print("-> parser has been deleted")

    def json_validation(self):
        validation_list = ('author', 'companyId', 'id', "indicators", "indicatorsIds", "isPublished",
                           "isTailored", "labels", "langs", "malwareList", "seqUpdate")
        for item in self.data:
            data_validation = all(item.get(key) is not None and item.get(key) != [] and
                                  item.get(key) != '' for key in validation_list)
            if data_validation:
                return True
        return False
