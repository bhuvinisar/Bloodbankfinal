from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', sign_in),
    path('register/', registerview, name='new'),
    path('search/', blood_search),
    path('datas/',blood_records),
    path('newpage/', newpage, name='forgot'),
    path('homepage/', homepage),
    path('login/', log_in)
]
