from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('login', views.login, name="login")
    #   path("path/name", views.TestFormCreate.as_view(), name="testformcreate")
]

urlpatterns += staticfiles_urlpatterns()
