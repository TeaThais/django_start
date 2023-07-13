from django.urls import path, re_path

from .views import about, contact, login, CatsHome, ShowCategory, ShowPost, AddNew

urlpatterns = [
    path('', CatsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_new/', AddNew.as_view(), name='add_new'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category')
]


