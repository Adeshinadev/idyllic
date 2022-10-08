from django.shortcuts import render
from product.models import Categorie, Product, Sub_categorie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.models import Product


# Create your views here.

def home(request):
    # return render(request, 'error.html')
    categories = Categorie.objects.all()
    return render(request, 'index.html', {'categories': categories})


def contact_us(request):
    categories = Categorie.objects.all()
    return render(request, 'contact_us.html', {'categories': categories})


def about_us(request):
    categories = Categorie.objects.all()
    return render(request, 'About.html', {'categories': categories})


def store(request):
    categories = Categorie.objects.all()
    product_obj = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_obj, 10)
    print(paginator)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    page2 = paginator.page(page)

    return render(request, 'shop.html',
                  {'categories': categories, 'products': products, 'paginator': paginator, 'page2': page2})


def sub_store(request, id):
    categories_obj = Categorie.objects.get(pk=id)
    categories = Sub_categorie.objects.filter(category=categories_obj)
    products = Product.objects.filter(sub_category__category=categories_obj)
    return render(request, 'sub_store1.html',
                  {'categories': categories, 'products': products, 'categories_obj': categories_obj})


def sub_store_sub_product(request, id):
    categories_obj = Sub_categorie.objects.get(pk=id)
    # categories = Sub_categorie.objects.filter(category=categories_obj)
    products = Product.objects.filter(sub_category=categories_obj)
    products_cat = Product.objects.filter(sub_category=categories_obj)[0]
    return render(request, 'sub_store2.html', {'products': products, 'products_cat': products_cat})


def handle_not_found(request, exception):
    return render(request, 'error.html')


def eaton(request):
    return render(request, 'eaton.html')


def fullriver(request):
    return render(request, 'fullriver.html')
