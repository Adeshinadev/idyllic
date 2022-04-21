"""secschoolportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('store', views.store, name='store'),
    path('store/<id>/', views.sub_store, name='store'),
    path('sub-product/<id>/', views.sub_store_sub_product, name='sub-product'),
]
