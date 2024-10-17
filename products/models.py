from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models ,product model


class Product(models.Model): 
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  price = models.IntegerField()
  category = models.CharField(max_length=100)
  stock_quantity = models.IntegerField()
  image_url = models.URLField(max_length=200)
  created_date = models.DateTimeField(auto_now=True)
  














# user model part

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

