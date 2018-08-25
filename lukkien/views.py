from django.shortcuts import render
from django.utils.html import format_html


def index(request):
    data = {
        'section': {'title': "Lukkien"},
        'h1': "Lukkien Django App",
        'text': "Use Shipping dropdown to create new objects in DB"
    }
    return render(request, 'shipping/base.html', data)
