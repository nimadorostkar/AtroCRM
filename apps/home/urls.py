from django.urls import path, re_path
from apps.home import views



app_name='app'



urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    # Product
    path('products', views.products, name='products'),
    #path('product_detail/<int:id>/',views.product_detail,name='product_detail'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
