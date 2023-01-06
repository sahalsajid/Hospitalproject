from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('dept',views.department,name='departments'),
    path('doct',views.doctors,name='doctors'),
    path('book',views.booking,name='booking'),
]
