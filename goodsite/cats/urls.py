from django.urls import path, re_path

from .views import about, add_new, contact, login, show_post, CatsHome, ShowCategory

urlpatterns = [
    path('', CatsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_new/', add_new, name='add_new'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category')
]


