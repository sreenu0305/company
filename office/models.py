""" models for project """
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Role(models.Model):
    """ different roles present in company which developed by super user"""
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Project(models.Model):
    """ models for project """
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class Application(models.Model):
    """ models for application where anyone can apply for job"""
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey(Role, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experiance_in_years = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """ models for registering employee who is verified by super user"""
    office = models.OneToOneField(Application, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    # qualification = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.office.name


class Team(models.Model):
    """ models for team in company """
    team_name = models.CharField(max_length=100)
    team_lead = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_working = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Gmail(models.Model):
    """ models for email """
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # sender = models.EmailField()
    # reciever = models.EmailField()
    body = models.TextField()
    subject = models.CharField(max_length=10000)
