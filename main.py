import datetime
import json
from flask import Flask, render_template, request
# from datetime import datetime

app = Flask(__name__)

# message1 = {
#     "text": "Как дела",
#     "sender": "Михаил",
#     "time": "19:20"
# }
#
# message2 = {
#     "text": "Дела - отлично",
#     "sender": "Василий",
#     "time": "19:21"
# }

# messages = []
DB_FILE = "./data/db.json" # Путь к файлу базы данных
db = open(DB_FILE, "rb") # ОТкрываем файлы для чтения
data = json.load(db) #Загрузка данных из файла в формате JSON
messages = data["messages"] # Из полученных данных берем поле 'messages'
    # {
    #     "text": "Как дела",
    #     "sender": "Михаил",
    #     "time": "19:20"
    # },
    # {
    #     "text": "Дела - отлично",
    #     "sender": "Василий",
    #     "time": "19:21"
    # }

# Сохранение всех сообщений в списке messages в файл
def save_messages_to_file():
    db = open(DB_FILE, "w") # Открываем файл для записи
    data = { # Создаем стуктуру для записи в файл
        "messages": messages
    }
    json.dump(data, db)  # Записываем структуру в файл

def add_message (text, sender): # Функция добавит сообщения в список
    now = datetime.datetime.now()
    new_message = {
        "text": text,
        "sender": sender,
        "time": now.strftime("%H:%M"), # Текущйи час и минуты
       #  "time": "23:59"
    }
    messages.append(new_message) #добавляем новое сообщение в список
    save_messages_to_file()

# print (message["sender"]) # Как обратитсья к полю в словаре

def print_message (message):
    print(f" [{message['sender']}]: {message['text']} / {message['time']}")
    # print(message["sender"])
    # print(message["time"])
    # print(message["text"])

# add_message("а еще долго будет идти", "Марина")
# add_message("Запятую надо убрать", "Вова")
#
# for message in messages:
#     print_message(message)

# Главная страница - аннотация пишется сразу над функцией
@app.route("/")
def index_page():
    return "Здравствуйте, вас приветствует СкиллЧат2022"

# Показать все сообщения в формате JSON
@app.route("/get_messages")
def get_messages():
    return {"messages": messages}

# Показать форму чата
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send_message")
def send_message():
    # Получить имя и текст от пользователя
    name = request.args["name"] # Получаем имя
    text = request.args["text"] # Получаем текст
    add_message(text, name)
    # Вызвать функцию add_message
    return "OK"

app.run() #Запускаем веб-приложение

#
# ПЛАН
# 1.  Создали внутреннюю возможность хранить сообщения, добавлять новые, читать чат
# 2.  Подключить визуальный интерфейс к нашим внутренним возможностям
#     - Преврать наш код в веб-сервер. Flask
#     - Созадть интерфейс и подключить его к веб-серверу

# print_message(message1)
# print_message(message2)


# messages = ["Всем привет", "Где я", "Продам гараж"]    # Список сообщений
#
# for text in messages:
#     print(f" - {text}")