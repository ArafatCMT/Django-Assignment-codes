from django.urls import path
from authors import views

urlpatterns = [
    path('register/', views.RegistrationForm, name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('changePassword/', views.ChangePassword, name='pass_change'),
    path('edit_profile/', views.UpdateProfile, name='edit_profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]