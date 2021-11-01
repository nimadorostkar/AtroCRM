from django.urls import path, re_path
from apps.home import views


#app_name='home'


urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    # Product
    path('products', views.products, name='products'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),

    # Customer
    path('customers', views.customers, name='customers'),
    path('customer_detail/<int:id>/',views.customer_detail,name='customer_detail'),

    # Order_request
    path('order_requests', views.order_requests, name='order_requests'),
    path('order_req_detail/<int:id>/',views.order_req_detail,name='order_req_detail'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
]
