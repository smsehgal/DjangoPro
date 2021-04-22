from django import forms
from django.contrib.auth.models import User
from login_form.models import UserProfileInfo
from django.core import validators


# class FormName(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
#     email = forms.EmailField()
#     text = forms.CharField(widget= forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget= forms.HiddenInput,
#                                  validators= [validators.MaxLengthValidator(0)])


class UserForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
