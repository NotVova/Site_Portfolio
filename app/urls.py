from django.urls import path

from .views import home, projects

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('projects/category/<int:category_id>/', projects, name='category'),
]
