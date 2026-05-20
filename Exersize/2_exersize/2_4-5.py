"""
Задача 5
Задание:
Напишите функцию-представление с именем home, которая возвращает текст Домашняя страница обрамлённый тегом h2.

"""
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Домашняя страница</h2>')