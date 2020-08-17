from django.shortcuts import render,get_object_or_404

from .models import Post
from .models import Category

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-id')[:]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def post_list(request):
    if request.method=='GET':
        category_id = (int)(request.GET.get('category_id',default='-1'))


        category_list = Category.objects.order_by('-id')[:]
        # 全部分类
        if category_id == -1:
            post_list = Post.objects.order_by('-id')[:]
        else:
            category = Category.objects.get(id=category_id)
            post_list = Post.objects.filter(Category=category)


    context = {'post_list': post_list, 'category_list': category_list}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def category_detail(request, category_id):
    category = Category.objects.get(id = category_id)
    post_list = category.post.all()
    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
        'post_list'  : post_list,
        'category_id'  : category_id,
    }
    return render(request, 'blog/category_list.html', context)

def about(request):
    context = {
    }
    return render(request, 'blog/about.html', context)