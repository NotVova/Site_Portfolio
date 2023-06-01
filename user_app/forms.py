from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from app.models import Article

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите Фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес ел. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    article = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    images = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control py-4'}))
    urls = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control py-4'}),
            'article': forms.TextInput(attrs={'class': 'form-control py-4'}),
            'images': forms.FileInput(attrs={'class': 'form-control py-4'}),
            'urls': forms.TextInput(attrs={'class': 'form-control py-4'}),
            'article_categories': forms.Select(attrs={'class': 'table table-sm', 'size': '3'})
        }
