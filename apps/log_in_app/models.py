from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class usersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["firstName"]) < 2:
            errors["firstName"] = "First Name Field must be atleast 2 characters long!"
        if len(postData["lastName"]) < 2:
            errors["lastName"] = "Last Name Field must be atleast 2 characters long!"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Email not valid format!"
        if len(postData["pw"]) < 8:
            errors["pw"] = "Password must be at least 8 characters long!"

        return errors


# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField( max_length=254)
    pw = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = usersManager()


class Messages(models.Model):
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(Users, related_name="messages")

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField(Messages, related_name="comments")
    users = models.ManyToManyField(Users, related_name="comments")
