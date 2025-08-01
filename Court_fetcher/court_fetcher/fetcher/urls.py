from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('fetch/<str:court>/<str:ctype>/<str:number>/<int:year>/', views.search, name='fetch_case_details'),
]
