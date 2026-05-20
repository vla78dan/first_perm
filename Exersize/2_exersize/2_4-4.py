"""

Задача 4
Дано содержимое файла представлений views.py приложения main_app:

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная')

def accounts(request, name='NoName', age=0):
    return HttpResponse(f'Имя: {name}, Возраст: {age}')


Задание:
Напишите содержимое файла urls.py приложения main_app. Добавьте следующие маршруты для функций представлений:

index(), чтобы функция выполнилась при посещении корневой директории сайта (например http://127.0.0.1:8000).
accounts(), чтобы функция выполнялась при посещении директорий сайта: /accounts/user_name/user_age/,
/accounts/user_name/ и /accounts/, где user_name это имя пользователя, и user_age это возраст пользователя.
Необходимо получить их в переменные name и age, указав для них спецификаторы str и int соответственно.
Например:
При переходе по ссылке http://127.0.0.1:8000/accounts/John/18/ должен быть выведен текст:  Имя: John, Возраст: 18
При переходе по ссылке http://127.0.0.1:8000/accounts/Tom/ должен быть выведен текст: Имя: Tom, Возраст: 0
При переходе по ссылке http://127.0.0.1:8000/accounts/ должен быть выведен текст: Имя: NoName, Возраст: 0
Используйте для этого функцию path(), предварительно импортировав её и файл представлений приложения.


"""

# from django.urls import path
# from main_app import views
#
# urlpatterns = [
#     path('', views.index),
#     path('accounts/', views.accounts),
#     path('accounts/<str:name>/<int:age>/', views.accounts),
#     path('accounts/<str:name>/', views.accounts),
# ]























