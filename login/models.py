from django.db import models
import re
from datetime import datetime, date

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        # if len(postData['first_name']) < 2:                                   # replaced with Bootstrap validations
        #     errors['first_name'] = "First Name must be at least 2 characters"
        
        # if len(postData['last_name']) < 2:
        #     errors['last_name'] = "Last Name must be at least 2 characters"

        # NAME_REGEX = re.compile(r'^[a-zA-Z\s.]+$')
        # if not NAME_REGEX.match(postData['first_name']):
        #     errors['first_name'] = "First Name may only contain letter characters"

        # NAME_REGEX = re.compile(r'^[a-zA-Z\s.]+$')
        # if not NAME_REGEX.match(postData['last_name']):
        #     errors['last_name'] = "Last Name may only contain letter characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email format!"
        
        all_users = User.objects.all()                  # section required to actually prevent entry of the email into db; AJAX gives user early notice
        for user in all_users:
            if postData['email'] == user.email:
                errors['email'] = "Email already in database. Choose another"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        
        dob = datetime.strptime(postData['birthday'], '%Y-%m-%d')
        def convert_dob_to_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        age = convert_dob_to_age(dob)
        print(age)
        if age < 13:
            errors['birthday'] = "Sorry, site is only for ages 13 and up"

        return errors


class User(models.Model): 
    fname = models.TextField()
    lname = models.TextField()
    email = models.TextField()
    birthday = models.DateField(default=date.today)     # new field added after original incept of class
    password = models.TextField()
    password_conf = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()     # replace the default value of objects = models.Manager() to custom version for validations
    # messages = a list of messages associated with a given User
    # user_comments = a list of comments associated with a given user

    def __repr__ (self):
        return f"<User Name: {self.fname} {self.lname} {self.birthday}>"




# Create your models here.
