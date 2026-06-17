from django.contrib import admin
from django.urls import path
from shop.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/<str:username>/', about)
]
