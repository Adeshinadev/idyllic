from django.shortcuts import render

from product.models import Product
from django.db.models import Q

# Create your views here.

def search(request):
    products=Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(sub_category__name__icontains=request.GET['q']) | Q(sub_category__category__name__icontains=request.GET['q']))
    return render(request, 'search.html', {'products':products,'q':request.GET['q']})
    