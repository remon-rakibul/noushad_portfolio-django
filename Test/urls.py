from django.urls import path

from Test import views

urlpatterns = [
    path('',views.index,name='index'),
    path('send_email/',views.send_email,name='send_email')
]


