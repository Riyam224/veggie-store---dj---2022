
from django.urls import path
from .views import ProductList , ProductDetail , newsletter_subscribe


app_name = 'products'

urlpatterns = [
    path('' , ProductList.as_view() , name='home'),
    path('<slug:slug>/' , ProductDetail.as_view() , name='detail'),
    path('newsletter/' ,newsletter_subscribe , name='newsletter_subscribe'),
   
]
