from django import forms
  
# creating a form
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, required=True)