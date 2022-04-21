from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from .models import Post
from product.models import Categorie
# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'blog.html'
    context_object_name = 'posts'

def PostList(request):
    queryset = Post.objects.all().order_by('-created_on')
    return render(request, 'blog.html', {'queryset': queryset, 'categories': Categorie.objects.all()})


def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    template_name = 'post-details.html'

    return render(request, template_name, {'post': post, 'categories': Categorie.objects.all()})