from django.contrib import admin
from django.urls import include, path
from sample import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('send-notes/', views.send_notes),
]