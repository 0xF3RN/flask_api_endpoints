from flask import Flask, request, Response
from flask_pymongo import PyMongo
from JsonParser import JSONParser
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/facct"
mongo = PyMongo(app)

'''
ну кароч что я тута сделал пока не забыл
1) я посмотрел джесон который мне дали и самое важное поле там - айтемс
тк я не уверен, что айтемс будет существовать я положил это в трай блок
2) мы сохраняем json в переменную, которую передаем при инициализации класса JSONparser
он в свою очередь проводит валидацию JSON файла на наличие полей, которые могут быть пустыми, или вовсе не существовать
3) дэбаг: в случае успешной проверки выводит файл, иначе возращает респонс с ошибкой
todo:
+ 0) сделай валидный джейсон, который далее в монгу будешь подгружать - done
+ 1) подключение к монгадб
+ 2) отправка даты в маонгу 
3) код ревью с колей

'''
'''
1) в трайблоке проискодит подключение к коллекции facct для последующего ее дополнения
далее создается лист, для хранения вставленных данных
далее получается сервер получает json файл для распарса
2) если успешно проходит проверка json файла на соотв поля и их заполненость
то начинается пополнение бд данными
3) в случае успеха возращает строку, где указаны id добавленных объектов и код 200
иначе код 400 - ошибка распарса
4) эксепшен на случай не предвиденных ошибок, чтобы сервер не упал

'''


@app.route('/api/add', methods=["POST"])
def api_add_data():
    try:
        collection = mongo.db.facct
        inserted_data_list = []
        parse_data = request.json.get("items", {})
        if JSONParser(parse_data).json_validation():
            #print(JSONParser(parse_data).print_data())
            for i in range(len(request.json["items"])):
                inserted_data = collection.insert_one(request.json["items"][i])
                inserted_data_list.append(inserted_data)
            return Response(f"Data has been successfully sent."
                            f" 'inserted_id(s)': {', '.join(str(i.inserted_id) for i in inserted_data_list)}.", 200)
        else:
            return Response("Error: make sure you have sent JSON file with valid information. Status: 400", 400)
    except Exception as e:
        return Response(f"error:{str(e)}. Status: 500", 500)


@app.route('/api/get')
def api_get():
    return Response("im existing")


if __name__ == '__main__':
    app.run(debug=True)
