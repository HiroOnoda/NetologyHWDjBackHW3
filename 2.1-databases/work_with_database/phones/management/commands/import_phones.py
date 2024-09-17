import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            #print(phone)
            # TODO: Добавьте сохранение модели
            new_phone = Phone(id = phone['id'],name = phone['name'],image = phone['image'],price = phone['price'],release_date = phone['release_date'],lte_exists = phone['lte_exists'])
            try:
                new_phone.save()
            except:
                print('Не удалось сохранить объект')
            else:
                try:
                    buf = Phone.objects.get(id=phone['id'])
                except:
                    print('no such obj')
                else:
                    print(buf.name)
