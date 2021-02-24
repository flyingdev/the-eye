from django.urls import path

from . import views


urlpatterns = [
    path('event/', views.aggregate, name='event-url'),
]
