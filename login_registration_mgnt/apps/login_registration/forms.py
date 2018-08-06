from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)



# r = RegistrationForm({'first_name':'Alex','last_name':'Moreno','email':'info@example.com','password':'asdfasdf','password_confrim':'asdfasdf'}