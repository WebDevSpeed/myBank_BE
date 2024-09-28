from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # For storing a hashed password
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    kk = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.username
