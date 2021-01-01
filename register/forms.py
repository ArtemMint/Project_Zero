from django import forms

from .models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
        labels = {
                'username':'Username:',
                'email':'E-Mail:',
                'password':'Password:',
                'picture':'Profile picture:',
                'first_name':'First name:',
                'last_name':'Last Name',
                'phone_number':'Mobile tel:',
                'country':'Country:',
                'address':'Address:',
                }
        fields = (
                'username',
                'email',
                'password',
                'picture',
                'first_name',
                'last_name',
                'phone_number',
                'country',
                'address',
                  )
        widgets = {
                'password': forms.PasswordInput(),
                  }

class SignInForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput())
