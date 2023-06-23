from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
#from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
def post_list(request):
    post_lists = Post.published.all()
    # постраничная разбивка с 3 постами на старнице
    paginator = Paginator(post_lists, 4)
    page_number = request.GET.get('page')  # если нет по такому юрл постарничной разбивки, переносит на 1 стр
    #posts = paginator.page(page_number)  #вызывая метода page получаем обьекты для желаемой страницы
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.page('1')
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'main/post/list.html',
                  {'posts': posts})

#первый способ если база данных не содержит значение по такому id
#def post_detail(request, id):
#    try:
#       post = Post.published.get(id=id)
#    except Post.DoesNotExist:
#        raise Http404('No post found ')
#
#    return render(request,
#                  'main/post/detail.html',
#                  {'post': post})

# Второй способ если база данных не содержит значение по такому id
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,)
    return render(request,
                  'main/post/detail.html',
                  {'post': post})



def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            error = 'Некорректно заполнено'

    form = PostForm()
    return render(request,
                  'main/post/create.html',
                  {'form': form,
                   'error': error})