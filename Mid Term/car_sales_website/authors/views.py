from django.shortcuts import render, redirect
from authors.forms import Registration, UserChangeData
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders import models
from cars.models import CarModel
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def RegistrationForm(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Registration(request.POST)
            if form.is_valid():
                form.save()
                # print(form.cleaned_data)
                messages.success(request, 'Account Created Successfully Please Login')
                return redirect('login')
        else:
            form = Registration()
        return render(request, 'registration.html', {'form': form})
    else:
        return redirect('profile')

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_redirect_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in Information is Incurrect')
        return super().form_invalid(form)

@login_required
def profile(request):
    object = models.Order.objects.filter(userID=request.user.id)
    # print(cars)
    cars = []
    for id in object:
        # print(id.carID, id.userID)
        cars.append(CarModel.objects.get(pk=id.carID))
    return render(request, 'profile.html', {'user': request.user, 'cars':cars})

class UserLogoutView(LogoutView):
    def get_redirect_url(self):
        messages.success(self.request, 'Logged out Successful')
        return reverse_lazy('homepage')

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user= request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html', {'form': form})

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        form = UserChangeData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
            return redirect('profile')
    else:
        form = UserChangeData(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})
