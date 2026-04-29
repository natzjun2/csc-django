from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")


def users(request):
    return render(request, "users.html")

def products(request):
    data = {
        "products": [
            {
                "id": 1,
                "product": "Laptop",
                "price": 500.00,
            },
            {
                "id": 2,
                "product": "Keyboard",
                "price": 20.00,
            },
            {
                "id": 4,
                "product": "Mouse",
                "price": 10.00,
            }
        ],
        "data":"hello",
        "name":"rodriguez"
    }
    return render(request, "products.html", data)