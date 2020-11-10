from django.db import models
import re	# the regex module

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        elif not postData["first_name"].isalpha():
            errors["first_name"] = "First name should be letters only"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        elif not postData["last_name"].isalpha():
            errors["last_name"] = "Last name should be letters only"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData["password"] != postData["confirm_pw"]:
            errors["confirm_pw"] = "Password and confirm password does not match"
        if self.filter(email=postData["email"]):
            errors["email"] = "Email is already registered"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # hidden messages
    objects = UserManager()
