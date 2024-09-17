from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    # for p in phones:
    #     print(type(p))
    #print(request.GET.get('sort'))
    sort_type = str(request.GET.get('sort'))
    if sort_type == 'min_price':
        phones = Phone.objects.all().order_by('price')
        pass
    elif sort_type == 'max_price':
        phones = Phone.objects.all().order_by('-price')
        pass
    else:
        phones = Phone.objects.all().order_by('name')
        pass
    context = {'phones':phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    prod = Phone.objects.get(slug =slug)
    context = {'phone':prod}
    return render(request, template, context)
