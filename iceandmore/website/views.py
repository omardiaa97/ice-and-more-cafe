from django.shortcuts import render
from .models import Item, Category
# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    items1 = Item.objects.filter(category__name="Drinks")
    items2 = Item.objects.filter(category__name="Icecream")
    items3 = Item.objects.filter(category__name="Fresh Juice")

    return render(request, 'website/index.html', {'items': items, 'items1': items1,'items2': items2,'items3': items3, 'categories': categories})