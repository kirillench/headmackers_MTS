from django.urls import path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    path('drevo/', drevo, name='drevo'),
    path('drevo/<int:drevo_id>/', drevo_detail, name='drevo_detail'),
    path('search/', search, name='search'),

]
