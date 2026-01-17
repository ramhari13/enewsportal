from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Category, Comment, Profile
from django.forms import ModelForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
         'username', 'email', 'password1', 'password2'
        ]


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'content', 'image', 'video', 'video_url', 'external_link', 'category']


#--user update form

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


        
#---Coment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
