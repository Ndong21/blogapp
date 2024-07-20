from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


# add a comment form
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Your Name'}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control', 'placeholder':'Leave a comment'}
        )
    )

# add a comment form
class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Post title'}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control', 'placeholder':'Write your post'}
        )
    )


# register a user (model form)
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    


# authenticate a user (model form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())        