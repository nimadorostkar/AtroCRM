from django.urls import path
from .views import login_view
from django.contrib.auth.views import LogoutView



#app_name='auth'



urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
