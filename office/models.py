""" models for project """
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    """ different roles present in company which developed by super user"""
    role = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)


class Team(models.Model):
    """ models for team in company """
    team_name = models.CharField(max_length=100)
    team_lead = models.CharField(max_length=100)


class Project(models.Model):
    """ models for project """
    project_name = models.CharField(max_length=100)
    teams_present = models.ForeignKey(Team, on_delete=models.CASCADE)


class Application(models.Model):
    """ models for application where anyone can apply for job"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey(Role, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experiance_in_years = models.IntegerField()
    is_verified = models.BooleanField(default=False)


class Employee(models.Model):
    """ models for registering employee who is verified by super user"""
    office = models.OneToOneField(Application, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    # qualification = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.IntegerField()


class Gmail(models.Model):
    """ models for email """
    sender = models.EmailField()
    reciever = models.EmailField()
    file = models.FileField(null=True, blank=True)
    body = models.TextField()
    subject = models.CharField(max_length=1000)
