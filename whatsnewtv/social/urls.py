from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("account", views.account_index, name="account"),
    path("search", views.search, name="search"),
    re_path(r'^(?P<type>movie|tv)/(?P<id>\d+)/?$', views.details, name="details"),
]
