from django.contrib import admin
from django.urls import path

from ads.views import root, AdListCreateView, AdDetailView

urlpatterns = [
     path('', AdListCreateView.as_view()),
     path('<int:pk>', AdDetailView.as_view())

]