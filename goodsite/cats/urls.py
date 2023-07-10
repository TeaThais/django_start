from django.urls import path, re_path

from .views import index, about, add_new, contact, login, show_post, show_category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_new/', add_new, name='add_new'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('cats/', index),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category')
]


