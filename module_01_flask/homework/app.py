import datetime
from flask import Flask
from random import choice
import random

app = Flask(__name__)


@app.route('/hello_world')
def hello_function():

    return 'Привет, мир!'


@app.route('/cars')
def cars_function():
    return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def cats_function():
    cats = ["корниш рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
    return choice(cats)


@app.route('/get_time/now')
def get_time_now_function():
    current_time = datetime.datetime.now()
    return "Точное время  " f"{current_time}"


@app.route('/get_time/future')
def get_time_future_function():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return "Точное время  " f"{current_time_after_hour}"


@app.route('/get_random_word')
def word_function():
    lines = random.choice(list(open('war_and_peace.txt', encoding='utf-8')))
    return lines


someGlobalVar = 0
@app.route('/counter')
def incrimentGlobalVar():
    global someGlobalVar
    someGlobalVar = someGlobalVar + 1
    return "Количество раз  " f"{someGlobalVar}"