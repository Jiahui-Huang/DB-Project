from django import forms

# class registerForm(forms.Form):
#     username = forms.CharField(required = False, max_length = 100)
#     email = forms.EmailField(required = True)
#     password = forms.CharField(required = False, max_length = 100)

class signinForm(forms.Form):
    username  = forms.CharField(required = False, max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)
