from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # move to 'forms.py'
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from cats.forms import *
from cats.models import Cats, Category, Menu
from .utils import *


class CatsHome(DataMixin, ListView):
    # paginate_by = 2    =>  method from ListView class
    model = Cats
    template_name = 'cats/for_view.html'
    context_object_name = 'posts'
   # extra_context = {'title': 'Main page'}  # for unchangeable data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cats.objects.filter(is_published=True).select_related('cat')
    # select_related to optimize sql queries with no duplicates with {p.cat}



class ShowCategory(DataMixin, ListView):
    model = Cats
    template_name = 'cats/for_view.html'
    context_object_name = 'posts'
    allow_empty = False   # to generate 404 when index doesn't exist

    def get_queryset(self):
        return Cats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=str(c.name),
                                      cat_selected=c.pk)
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


class AddNew(LoginRequiredMixin, DataMixin, CreateView):
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cats/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *,  object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    # to get user logged in after registration
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cats/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'cats/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Contact')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def about(request):
    return render(request, 'cats/about.html', {'title': 'About', 'menu': Menu.objects.all()})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Этой страницы нигде неть</h2>')


