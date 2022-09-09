from django import forms as f



class Administrators_Login(f.Form):
    username = f.CharField(max_length=200, min_length=3, widget=f.TextInput(attrs={
        "placeholder": "Username", 
        "title": "Enter the username Demiz gave you"
    }))
    password = f.CharField(max_length=50, min_length=5, widget=f.PasswordInput(attrs={
        "placeholder": "Password", 
        "title": "Enter the password Demiz gave you"
    }))
    