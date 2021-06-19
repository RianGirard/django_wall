from django.urls import path
from . import views 

urlpatterns = [
    path('', views.wall),
    path('enter_message', views.enter_message),
    path('enter_comment', views.enter_comment),
    # path('delete_message', views.delete_message),             # former url used with form POST request; turned off for AJAX version
    path('delete_message/<str:message_id>', views.delete_message),
    path('logoff', views.logoff),
]