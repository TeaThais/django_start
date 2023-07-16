from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from cats.forms import *
from cats.models import Cats, Category, Menu
from .utils import *


class CatsHome(DataMixin, ListView):
    model = Cats
    template_name = 'cats/for_view.html'
    context_object_name = 'posts'
   # extra_context = {'title': 'Main page'}  # for unchangeable data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cats.objects.filter(is_published=True)

# def index(request):
#     context = {
#         'title': 'Main page',
#         'cat_selected': 0
#     }
#     return render(request, 'cats/index.html', context=context)


class ShowCategory(DataMixin, ListView):
    model = Cats
    template_name = 'cats/for_view.html'
    context_object_name = 'posts'
    allow_empty = False   # to generate 404 when index doesn't exist

    def get_queryset(self):
        return Cats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        c_def = self.get_user_context(title=str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#
#     context = {
#         'category': category,
#         'title': 'Selected cats',
#         'cat_selected': category.id
#     }
#     return render(request, 'cats/index.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = Cats
    template_name = 'cats/post_complete.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self):
        return Cats.objects.filter(slug=self.kwargs['post_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_post(request, post_slug):
#     post = get_object_or_404(Cats, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'cats/post_complete.html', context=context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})


class AddNew(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'cats/add_new.html'
    success_url = reverse_lazy('home')    # after adding shows homepage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add new cat')
        return dict(list(context.items()) + list(c_def.items()))

# def add_new(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Cats.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'cats/add_new.html', {'form': form, 'title': 'Add new cat'})


def contact(request):
    return HttpResponse('Contact Us')


def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Этой страницы нигде неть</h2>')
