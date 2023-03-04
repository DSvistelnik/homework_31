from users.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from users.views import LocationViewSet

#location_router = routers.SimpleRouter()
#location_router.register("location", LocationViewSet)

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('<int:pk>/update/', UserUpdateViews.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),


]

#urlpatterns += location_router.urls
