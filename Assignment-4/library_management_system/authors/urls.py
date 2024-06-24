from django.urls import path
from authors.views import RegistrationFormView, UserLoginView, UserLogoutView, profile
urlpatterns = [
    path('register/', RegistrationFormView.as_view(),  name='register'),
    path('login/', UserLoginView.as_view(),  name='login'),
    path('logout/', UserLogoutView.as_view(),  name='logout'),
    path('profile/', profile,  name='profile'),
]