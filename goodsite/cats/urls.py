from django.urls import include, path

from .views import about, contact, CatsHome, ShowCategory, ShowPost, AddNew, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', CatsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_new/', AddNew.as_view(), name='add_new'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
    path("__debug__/", include("debug_toolbar.urls"))
]


