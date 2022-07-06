from django.urls import path
from . import views
urlpatterns=[
    path('base/',views.index,name='base'),
    path('homepage/',views.homepage,name='homepage'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact/',views.sendemail,name='contact')
]