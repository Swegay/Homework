from django.shortcuts import render
from .models import Product
# Create your views here.
def get_ingex_page(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def get_product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'shop/product-details.html', {'product': product})