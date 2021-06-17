from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index),
    path ('register', views.register),
    path ('login', views.login),
    path ('success', views.success),
    path ('email_valid/', views.email_valid_null),       # this is here for case of zero text value entry
    path ('email_valid/<str:email>', views.email_valid),
    path ('email_regex/', views.email_regex_null),
    path ('email_regex/<str:email>', views.email_regex),
    path ('age_valid/<str:birthday>', views.age_valid),
    path ('logout', views.logout),
]