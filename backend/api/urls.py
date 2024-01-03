from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
]

