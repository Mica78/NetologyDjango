from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', '')
    phones = Phone.objects.all()
    match sort:
        case 'name':
            phones = Phone.objects.all().order_by('name')
        case 'min_price':
            phones = Phone.objects.all().order_by('price')
        case 'max_price':
            phones = Phone.objects.all().order_by('-price')
        case '':
            phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
