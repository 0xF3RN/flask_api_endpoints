from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from JsonParser import JSONParser
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/facct"
mongo = PyMongo(app)


@app.route('/api/v2/add/data', methods=["POST"])
def api_add_data():
    try:
        collection = mongo.db.facct
        inserted_data_list = []
        parse_data = request.json.get("items", {})
        if JSONParser(parse_data).json_validation():
            for i in range(len(request.json["items"])):
                inserted_data = collection.insert_one(request.json["items"][i])
                inserted_data_list.append(inserted_data)
            return Response(f"Data has been successfully sent."
                            f" 'inserted_id(s)': {', '.join(str(i.inserted_id) for i in inserted_data_list)}.", 200)
        else:
            return Response("Error: make sure you have sent JSON file with valid information. Status: 400", 400)
    except Exception as e:
        return Response(f"Error: {str(e)}. Status: 500", 500)


@app.route('/api/v2/get/data', methods=['GET'])
def api_get():
    try:
        collection = mongo.db.facct
        params = request.args.to_dict()
        data = list(collection.find())
        if data:
            return jsonify(dumps(data))
        else:
            data = list(collection.find({"indicators": {"$elemMatch": params}}))
            if data:
                return jsonify(dumps(data))
            else:
                return jsonify({"Message": "No data found"})
    except Exception as e:
        return jsonify({"Error": e})


if __name__ == '__main__':
    app.run(debug=True)
