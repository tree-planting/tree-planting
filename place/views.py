import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import (
    Place,
)

def index(request):
    return redirect('https://bit.ly/tree-taiwan-sites')

def detail_api(request, pk):
    item = Place.objects.get(pk=pk)
    return HttpResponse(
        json.dumps(item.tojson()),
        content_type="application/json"
    )

def detail(request, pk):
    item = Place.objects.get(pk=pk)

    return render(request, 'layout.html', context={
        'item': item})
