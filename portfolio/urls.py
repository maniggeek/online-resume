from django.urls import path
from .views import PageView
from .views import SuccessView


urlpatterns = [
    path('',PageView.as_view(),name='index'),
    path('success/',SuccessView.as_view(),name='success'),
]
