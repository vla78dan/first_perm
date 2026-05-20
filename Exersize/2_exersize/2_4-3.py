"""
Задача 3
Дано содержимое файла представлений views.py приложения main_app:
________________________________________________________
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная</h1>')

def accounts(request, name):
    return HttpResponse(f'<h1>Имя: {name}</h1>')
    ______________________________________________________
Задание:
Напишите содержимое файла urls.py приложения main_app. Добавьте следующие маршруты для функций представлений:

index(), чтобы функция выполнилась при посещении корневой директории сайта (например http://127.0.0.1:8000).
accounts(), чтобы функция выполнилась при посещении директории сайта /accounts/user_name/ (например http://127.0.0.1:8000/accounts/Tom/), где user_name это имя пользователя, необходимо получить его в переменную name, обязательно указав спецификатор str.
Используйте для этого функцию path(), предварительно импортировав её и файл представлений приложения.


"""
# from django.urls import path
# from main_app import views
#
# urlpatterns = [
#     path('', views.index),
#     path('accounts/<str:name>/', views.accounts),
# ]