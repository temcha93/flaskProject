"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
import datetime
print(datetime.datetime.today().weekday())
"""

from datetime import date
from datetime import time
from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username) -> str:
    today = datetime.now()
    # выводим (today)
    # Получаем текущее время
    # t = datetime.time(datetime.now())
    # выводим "The current time is", t
    # день недели от 0 (понедельник) до 6 (воскресенье)
    wd = date.weekday(today)
    # Дни начинаются с 0 для понедельника
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return f"Привет, {username} Хорошей {days[wd]}!"


if __name__ == "__main__":
    app.run(debug=True)
