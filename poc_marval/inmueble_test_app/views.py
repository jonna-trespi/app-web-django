import requests
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def load_products(request):
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()[:5]  # Trae solo 5 productos
    return render(request, "product_list.html", {"products": products})