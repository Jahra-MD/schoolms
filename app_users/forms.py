from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo ,CCAProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

       

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')

class CCAProfileInfoform(forms.ModelForm):
    des =forms.CharField(required=True)
   
    class Meta():
        model = CCAProfileInfo
        fields=('des','cca_pic','name') 
    
