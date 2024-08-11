from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    content = []
    with open(settings.BUS_STATION_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content.append({'Name':row['Name'],'Street':row['Street'],'District':row['District']})
    paginator = Paginator(content,10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
