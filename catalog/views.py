from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home_view(request):
    list_product = Product.objects.all
    context = {"products": list_product}
    return render(request, 'home.html', context)

def contacts_view(request):
    return render(request, 'contacts.html')

def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)

