from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
author = {
       "Имя": "Иван",
       "Отчество": "Петрович",
       "Фамилия": "Иванов",
       "телефон": "8-923-600-01-02",
       "email": "vasya@mail.ru",
}

def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
       <header>
       / <a href="/"> Home </a> / <a href="/items"> Items </a> / <a href="/about"> About </a>
       </header><br>
       Имя: <b>{author['Имя']}</b><br>
       Отчество: <b>{author['Отчество']}</b><br>
       Фамилия: <b>{author['Фамилия']}</b><br>
       телефон: <b>{author['телефон']}</b><br>
       email: <b>{author['email']}</b><br>
       """
    return HttpResponse(text)


def get_item(request, item_id: int):
    """ По указанному item_id возращаем имя элемента и количество. """
    try:
        item = Item.objects.get(id=item_id) 
        if item :
            context = {
                "item":  item
            }
            return render(request, "item_page.html", context)
    except ObjectDoesNotExist:    
        return HttpResponseNotFound(f'Item with id={item_id} not found')


def get_items(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items_list.html", context)