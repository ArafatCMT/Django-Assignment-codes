from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from authors.forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from library.models import Borrow, Book


# Create your views here.
class RegistrationFormView(FormView):
    template_name = 'authors/register_form.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'authors/login_form.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class UserLogoutView(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy('login')

@login_required
def profile(request):
    borrow = Borrow.objects.filter(userId=request.user.id)
    books = []
    for pair in borrow:
        # print(pair.bookId, pair.userId)
        book = Book.objects.get(id=pair.bookId)
        books.append(book)
    
    return render(request, 'authors/profile.html', {'books': books})


