from django.urls import path
from django.conf.urls import url
from .views import (
    ItemDetailView,
    HomeView,
    item_list,
)

app_name = 'core'

urlpatterns = [
    #path('', HomeView.as_view(), name='home'),
    path('', item_list, name='home'),
]
