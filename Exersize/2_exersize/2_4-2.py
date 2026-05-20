"""
Дано содержимое файла представлений views.py приложения main_app:

from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Главная</h1>')


def catalog(request):
    return HttpResponse('<h1>Каталог</h1>')


def contact(request):
    return HttpResponse('<h1>Контакты</h1>')


Задание:
Напишите содержимое файла urls.py приложения main_app. Добавьте следующие маршруты для функций представлений:

index(), чтобы функция выполнилась при посещении корневой директории сайта (например http://127.0.0.1:8000).
catalog(), чтобы функция выполнилась при посещении директории сайта /catalog/ (например http://127.0.0.1:8000/catalog/).
contact(), чтобы функция выполнилась при посещении директории сайта /contact/ (например http://127.0.0.1:8000/contact/).
Используйте для этого функцию path(), предварительно импортировав её и файл представлений приложения.
"""

# from django.urls import path
# from main_app import views
#
# urlpatterns = [
#     path('', views.index),
#     path('catalog/', views.catalog),
#     path("contact/", views.contact),
# ]













