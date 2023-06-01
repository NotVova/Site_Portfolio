from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from .forms import (ArticleForm, UserLoginForm, UserProfileForm,
                    UserRegistrationForm)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    contex = {
        'form': form,
        'title': 'Авторизация',
    }

    return render(request=request, template_name='user_app/login.html', context=contex)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
        'title': 'Регистрация',
    }

    return render(request=request, template_name='user_app/registration.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Личный кабинет',
        'form': form,
    }

    return render(request=request, template_name='user_app/profile.html', context=context)


def article(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('article'))
        else:
            print('Ошибка')
    else:
        form = ArticleForm()

    context = {
        'title': 'Статьи',
        'form': form,
    }

    return render(request=request, template_name='user_app/article.html', context=context)
