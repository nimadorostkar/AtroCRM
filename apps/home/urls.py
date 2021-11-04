from django.urls import path, re_path
from apps.home import views



urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('etc', views.etc, name='etc'),
    path('search',views.search,name='search'),
    # Product
    path('products', views.products, name='products'),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
    # Customer
    path('customers', views.customers, name='customers'),
    path('customer_detail/<int:id>/',views.customer_detail,name='customer_detail'),
    path('customer_registration', views.customer_registration, name='customer_registration'),
    path('customer_edit/<int:id>/', views.customer_edit, name='customer_edit'),
    # Order
    path('order_requests', views.order_requests, name='order_requests'),
    path('order_req_detail/<int:id>/',views.order_req_detail,name='order_req_detail'),
    path('order_registration', views.order_registration, name='order_registration'),
    path('order_edit/<int:id>/', views.order_edit, name='order_edit'),
]
