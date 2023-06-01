from django.urls import path

from .views import article, login, logout, profile, registration

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('loguot/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('article/', article, name='article')
]
