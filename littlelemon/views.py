from django.shortcuts import render, get_object_or_404
from .models import Menu


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    return render(request, 'book.html')


def menu(request):
    menu_items = Menu.objects.all().order_by('name')
    context = {'menu': menu_items}
    return render(request, 'menu.html', context)


def menu_item(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)
    context = {'menu_item': menu_item}
    return render(request, 'menu_item.html', context)
