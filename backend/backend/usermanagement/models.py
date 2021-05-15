from django.db import models
from django.contrib.auth.hashers import make_password


# Access type model
class AccessType(models.Model):
    class Meta:
        db_table = 't_access_type'
        ordering = ['ins_timestamp']
    access_id = models.BigAutoField(primary_key=True)
    access_name = models.CharField(max_length=255)
    ins_timestamp = models.DateTimeField(auto_now_add=True)
    upd_timestamp = models.DateTimeField(auto_now=True)


# User model
class User(models.Model):
    class Meta:
        db_table = 't_user'
        ordering = ['ins_timestamp']
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    profile_picture = models.FilePathField(path='/media')
    ins_timestamp = models.DateTimeField(auto_now_add=True)
    upd_timestamp = models.DateTimeField(auto_now=True)
    access_types = models.ManyToManyField(AccessType)

    def set_password(self, password):
        self.password = make_password(password)
        return self

# @author Simon Peter Calamno
# @since 2021.05.15
