from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('requestcall/',requested,name='requested'),
    path('signin/',signin,name='signin'),
]