from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm

def index(request):
    categories = Category.objects.all()
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'categories' : categories,
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var
    }
    return render(request, 'index.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = blog
            form.save()
            return redirect('blog', blog_id=blog_id)
    context = {
        'blog' : blog,
        'form' : form,
    }
    return render (request, 'blog.html', context)

def CategoryView(request, cats):
    category_post = Post.objects.filter(categories__title__contains=cats)
    context = {
        'cats' : cats,
        'category_post' : category_post
    }
    return render(request, 'categories.html', context)