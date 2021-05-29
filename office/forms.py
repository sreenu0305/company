from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from office.models import Application, Employee, Team, Project, Gmail


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        # fields = "__all__"
        fields = ['name', 'email', 'designation', 'qualification', 'experiance_in_years']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class GmailForm(ModelForm):
    class Meta:
        model = Gmail
        fields =['reciever','subject','body']


# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
