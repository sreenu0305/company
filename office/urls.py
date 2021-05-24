from django.urls import path
from office import views

urlpatterns = [
    # path('',views.maim,name='main'),
    path('register/',views.register_request,name='register'),
    path('',views.login_request,name='login'),
]