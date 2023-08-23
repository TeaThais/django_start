from django.urls import include, path
from django.views.decorators.cache import cache_page
from .views import about, CatsHome, ShowCategory, ShowPost, AddNew, RegisterUser, LoginUser, logout_user, \
    ContactFormView

urlpatterns = [
    path('', cache_page(10)(CatsHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('add_new/', AddNew.as_view(), name='add_new'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/',  cache_page(60 * 2)(ShowPost.as_view()), name='post'),
    path('category/<slug:cat_slug>/',  ShowCategory.as_view(), name='category'),
    path("__debug__/", include("debug_toolbar.urls"))
]


