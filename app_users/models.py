from django.db import models
from django.contrib.auth.models import User
import os

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)
    
    if instance.cca_pic:
        filename = 'CCA_Profile_Pictures/{}.{}'.format(instance.cca_pic,ext)
    return os.path.join(upload_to, filename)


class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username

class CCAProfileInfo( models.Model):
    name =models.CharField(max_length=100,blank=False)
    des =models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    cca_pic =models.ImageField(upload_to =path_and_rename,verbose_name='poster',blank=True)

