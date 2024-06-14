from django.urls import path
from cars import views

urlpatterns = [
    path('details/<int:id>/', views.CarDetailView.as_view(), name='details'),
    path('update/<int:id>/', views.PostUpdateView, name='update'),
]
