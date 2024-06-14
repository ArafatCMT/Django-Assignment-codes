from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from car_sales_website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'homepage'),
    path('brand/<slug:slug>', views.home, name= 'brand_wise_car'),
    path('author/', include('authors.urls')),
    path('orders/', include('orders.urls')),
    path('cars/', include('cars.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
