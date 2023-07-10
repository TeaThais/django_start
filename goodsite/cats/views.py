from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from cats.forms import *
from cats.models import Cats, Category, Menu


def index(request):

    context = {
        'title': 'Main page',
        'cat_selected': 0
    }
    return render(request, 'cats/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Cats, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'cats/post_complete.html', context=context)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)

    context = {
        'category': category,
        'title': 'Selected cats',
        'cat_selected': category.id
    }
    return render(request, 'cats/index.html', context=context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})


def add_new(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
                # Cats.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'cats/add_new.html', {'form': form, 'title': 'Add new cat'})


def contact(request):
    return HttpResponse('Contact Us')


def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Этой страницы нигде неть</h2>')
