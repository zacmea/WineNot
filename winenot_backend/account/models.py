import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

#Class for managing custom users
class CustomUserManager(UserManager): # CustomUserManager inherits from UserManager
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

#General User class, customized to use email as the username
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    # wine_collections = models.ManyToManyField(WineCollection, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_namew
    
    def __str__(self):
        return self.email

#Class for storing wine data, based on data that will be avail from Vivino API
class Wine(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    thumb = models.URLField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_ratings = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
#Class for storing collections of wines
class WineCollection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wines = models.ManyToManyField(Wine, blank=True)

    def __str__(self):
        return self.name
