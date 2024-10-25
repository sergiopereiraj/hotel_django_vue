from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class Contestant(models.Model):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return True
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
