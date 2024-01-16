from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

author = {
      "Имя     ": "Иван",
      "Отчество": "Петрович",
      "Фамилия ": "Иванов",
      "телефон ": "8-923-600-01-02",
      "email   ": "vasya@mail.ru",
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def text(requst):
    return render(requst,'index.html')
    

def about(request):
    return HttpResponse(
        """<p>Имя: <strong>Иван</strong></p>
<p>Отчество: <strong>Петрович</strong></p>
<p>Фамилия: <strong>Иванов</strong></p>
<p>телефон: <strong>8-923-600-01-02</strong></p>
<p>email: <strong>vasya@mail.ru</strong></p>
"""
    )

def about1(request):
    text =f"""Имя: <b>{author['Имя']}</b><br>
<p>Отчество: <b>{author['Отчество']}</b><br>
<p>Фамилия: <b>{author['Фамилия']}</b><br>
<p>телефон: <b>{author['телефон']}</b><br>
<p>email:   <b>{author['email']}</b><br>
"""
    return HttpResponse(text)

def get_item(request, item_id: int):
    """по указанному id возвращаем товар"""
    for item in items:
        if item['id']==item_id:
            item_name = F"""
            <p>name: <b>{item['name']}</b><br>
            <p>quantity: <b>{item['quantity']}</b><br>"""
            return render(request,'itemlist.html',context)
    return HttpResponseNotFound(f"not found {item_id}")


def items_(request):
    items_li = '<ol>'
    for item in items:
        items_li += f"""<li><a href="/item/{item['id']}">Имя: {item['name']}</a></li>"""
    items_li += '</ol>'
    return HttpResponse(items_li)

                    
    