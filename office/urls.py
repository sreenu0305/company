from django.urls import path
from office import views

urlpatterns = [
    path('',views.main,name='main'),
    # path('register/',views.register_request,name='register'),
    path('login/',views.login_request,name='login'),
    path('apply/',views.apply,name='apply'),
    path('save_application/',views.save_application,name='save_application'),
    path('registration/',views.registration,name='registration'),
    path('details/',views.employee_details,name='details'),
    path('save_register/',views.save_register,name='save-register'),

]