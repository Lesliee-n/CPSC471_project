from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('test/', views.test, name='test'),
    path('movie_showcase/', views.movie_showcase, name='movie_showcase'),
    path('ticket_page/', views.ticket_page, name='ticket_page'),
    path('concession_order/', views.concession_order, name='concession_order')
]