from django.urls import path

from . import views

urlpatterns = [
	path('', views.InfoOverview, name='api'),
	path('info-list/', views.InfoList, name='info-list'),
	path('info-detail/<str:pk>', views.InfoDetail, name='info-detail'),
	path('info-create/', views.InfoCreate, name='info-create'),
]