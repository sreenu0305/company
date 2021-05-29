""" views for project """
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages

from office.forms import ApplicationForm, EmployeeForm, TeamForm, ProjectForm, GmailForm
from office.models import Application, Employee, Team, Project
from django.conf import settings


def main(request):
    """ views of main page """
    return render(request, 'office/index.html')


def apply(request):
    """ views for application"""
    form = ApplicationForm
    return render(request, 'office/application.html', {'form': form})


def save_application(request):
    """ to save application"""
    if request.method == 'POST':
        form_obj = ApplicationForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return render(request, 'office/index.html', {'form': ApplicationForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/office/')


def registration(request):
    """ for registration"""
    form = EmployeeForm
    return render(request, 'office/registration.html', {'form': form})


def save_register(request):
    """ save registration form"""
    if Application.objects.filter(email=request.POST['email'], is_verified=True).exists():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'])
        office = Application.objects.get(email=request.POST["email"])
        Employee.objects.create(phone=request.POST['phone'], image=request.FILES['image'],
                                salary=request.POST['salary'], email=request.POST['email'], user=user, office=office)
        return HttpResponseRedirect('/office/')
    else:
        return render(request, 'office/application.html', {'error': 'you are not eigible for this job'})


def password_reset_request(request):
    """ for reset password"""
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request,
                                     'A message with reset password instructions has been sent to your inbox.')
                    return redirect("main:homepage")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="office/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


# def maim(request):
#     return render(request, 'office/index.html')


# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("office/main/")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm
#     return render(request, "office/register.html", {'form': form})

def login_user(request):
    """ login page"""
    return render(request, 'office/login.html')


def login_request(request):
    """ save login details"""

    username = request.POST['username']
    password = request.POST['password']
    # email = request.POST['email']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if Employee.objects.filter(user=user).exists():
            return HttpResponseRedirect('/office/details/')
        else:
            return render(request, 'office/login.html', {'error': 'Invalid username or password'})

    else:
        return render(request, 'office/login.html', {'error': 'Invalid username or password'})


def employee_details(request):
    """ login request"""
    user = request.user
    gmail = user.email
    print(gmail)
    data = Employee.objects.get(email=gmail)
    x = data.office.designation
    print(x.role)
    # print(type(x.role))
    import pdb
    # pdb.set_trace()

    # emp = False
    if x.role == 'CEO' or 'HR':
        emp = True
        # pdb.set_trace()
        # return render(request, 'office/index.html')

    return render(request, 'office/permission.html', {'user': user, 'data': data, 'emp': emp})
    # else:

    # return render(request, 'office/permission.html', {'data': data, 'user': user, 'emp': emp})
    #     return render(request, 'office/details.html', {'user': user, 'form': data})
    # return render(request, 'office/index.html')


def application_permission(request):
    """ giving acceptance for applications"""
    data = Application.objects.filter(is_verified=False)

    import pdb
    # pdb.set_trace()
    # print(data.name)

    return render(request, 'office/accept.html', {'data': data})


def applied_details(request, id):
    """ application details"""
    data = Application.objects.get(id=id)
    return render(request, 'office/applied.html', {'data': data})


def total_teams(request):
    """ total teams list """
    data = Team.objects.all()
    import pdb
    # pdb.set_trace()
    return render(request, 'office/total_team.html', {'data': data})


def team(request):
    """ for  creating teams """
    form = TeamForm
    return render(request, 'office/team.html', {'form': form})


def save_team(request):
    """ saving team """
    if request.method == 'POST':
        form_obj = TeamForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return render(request, 'office/permission.html', {'form': TeamForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/office/')


def total_projects(request):
    """ total projects """
    data = Project.objects.all()

    return render(request, 'office/project_list.html', {'data': data})


def project(request):
    """ creating project """
    form = ProjectForm()
    return render(request, 'office/project.html', {'form': form})


def save_project(request):
    """ saving project-"""
    if request.method == 'POST':
        form_obj = ProjectForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return render(request, 'office/permission.html', {'form': TeamForm(), 'error': form_obj.errors})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/office/login_page/')


def sent_mail(request):
    data = Employee.objects.all()
    # mails = data.office.email
    form = GmailForm
    # import pdb
    # pdb.set_trace()
    return render(request, 'office/email.html', {'form': form, 'mail': data})


def save_mail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('message')
        reciever = request.POST.get('email')
        send_mail(subject, body, settings.EMAIL_HOST_USER,
                  [reciever], fail_silently=False)
        return render(request, 'office/mail_sent.html', {'email': reciever})

    return render(request, 'office/index.html', {})


def employ_list(request):
    data = Employee.objects.all()
    return render(request, 'office/emp_list.html', {'data': data})


def emp_details(request, id):
    data = Employee.objects.get(id=id)
    return render(request, 'office/emp_details.html', {'data': data})
