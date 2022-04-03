from django.shortcuts import render, redirect
from phones.models import Phone


def index():
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        result = phone.order_by('name')
    elif sort == 'min_price':
        result = phone.order_by('price')
    elif sort == 'max_price':
        result = phone.order_by('price').reverse()
    else:
        result = phone

    context = {'phone': result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
