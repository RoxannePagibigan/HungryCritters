from django.db import models
from datetime import datetime
import re
import bcrypt

class UserManager(models.Manager):
    def RegistrationValidator(self, postData):
        errors = {}

        # length of first name
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"

        # length of last name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"

        # length of password
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"

        # email format
        UserRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not UserRegex.match(postData['email']):
            errors['email'] = "Invalid email address"

        # email is unique
        CheckEmail = User.objects.filter(email = postData['email'])
        if len(CheckEmail) > 0:
            errors['emailExists'] = "Email already in use by another user in our system"

        # password matches
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match"

        # user's age is greater than 13
        if postData['birthday'] > '2008-01-01 00:00:00':
            errors['birthday'] = "User must be at least 13 years old"

        # date is in the past
        if datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.now():
                errors['birthday'] = 'Date should be in the past'
        return errors
    
    def LoginValidator(self, postData):
        errors = {}

        LoggedUser = User.objects.filter(email=postData['email'])
        if len(LoggedUser) > 0:

            # password and email match
            if bcrypt.checkpw(postData['password'].encode(), LoggedUser[0].password.encode()):
                print("Password matches")
            else:
                # password and email do not match
                errors['password'] = "Email Address and password do not match!"
        else:
            # user doesn't exist
            errors['email'] = "There is no user with that email"

        # email format
        UserRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not UserRegex.match(postData['email']):
            errors['email'] = "Invalid email address"
        return errors

    def UpdateValidator(self,postData):
        errors = {}

        # length of first name
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"

        # length of last name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"

        # email format
        UserRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not UserRegex.match(postData['email']):
            errors['email'] = "Invalid email address"
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    birthday = models.DateTimeField(default=datetime.now())
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name
