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
    path('login_page/',views.login_user,name='save-login_page'),
    path('accept/',views.application_permission,name='application_accept'),
    path('<int:id>/applied/',views.applied_details,name='application_accept'),
    path('team/',views.team,name='team'),
    path('save_team/',views.save_team,name='save_team'),
    path('project/',views.project,name='project'),
    path('save_project/',views.save_project,name='save_project'),
    path('total_teams/',views.total_teams,name='total_teams'),
    path('total_projects/',views.total_projects,name='total_projects'),
    path('logout/',views.logout_page,name='logout'),
    path('sent_mail/',views.sent_mail,name='sent_mail'),
    path('save_mail/',views.save_mail,name='save_mail'),
    path('emp_list/',views.employ_list,name='emp_list'),
    path('<int:id>/emp_details/',views.emp_details,name='emp_details'),
    path('<int:id>/emp_accept/',views.accept,name='emp_accept'),

]