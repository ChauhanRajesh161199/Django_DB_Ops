from django.urls import path
from Simple import views

urlpatterns = [
    path('', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name='testing'), 
]