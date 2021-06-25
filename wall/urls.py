from django.urls import path
from . import views 

urlpatterns = [
    path('', views.wall),
    path('enter_message', views.enter_message),
    path('enter_comment', views.enter_comment),
    path('delete_message', views.delete_message),
    path('delete_comment', views.delete_comment),
    path('logoff', views.logoff),
]