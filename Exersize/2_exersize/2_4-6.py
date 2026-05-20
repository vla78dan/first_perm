"""
Задача 6
Задание:
Напишите функцию-представление с именем message, которая будет принимать параметры category, subcategory, theme, number из маршрута и возвращать их в виде маркированного списка. Слово Сообщение должно быть обрамлено тегом h2.

Например, при значениях category='Программирование', subcategory='Python', theme='Django 4' и number=12, результат работы данной функции должен выглядеть так:




P.S. На экран ничего не нужно выводить, для многострочных строк использовать только двойные кавычки . Код структуры HTML-страницы не нужен (теги <html>, <head>, <body>).

"""

from django.http import HttpResponse

# def message(request, category, subcategory, theme, number):
#     return HttpResponse(f"""
#     <ul>
#     <h2>Сообщение</h2>
#     <li>Категория: {category}</li>
#     <li>Подкатегория: {subcategory}</li>
#     <li>Тема: {theme}</li>
#     <li>Номер сообщения: {number}</li>
#     </ul>
# """)
#
# from django.http import HttpResponse
#
# def message(request, category, subcategory, theme, number):
#     return HttpResponse(f'<h2>Сообщение</h2><ul><li>Категория: {category}</li><li>Подкатегория: {subcategory}</li><li>Тема: {theme}</li><li>Номер сообщения: {number}</li></ul>')