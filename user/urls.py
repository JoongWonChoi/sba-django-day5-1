from django.urls import path
from . import views

urlpatterns =[
        path('second/',views.index),
        path('register/',views.register),
        path('mysite/', views.mysite),
        path('form/',views.formtest),
        path('git/',views.git)

        ]
