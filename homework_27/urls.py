"""homework_27 URL Configuration

"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import LocationViewSet

location_router = routers.SimpleRouter()
location_router.register("location", LocationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ads.urls")),
    path('user/', include("users.urls")),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]
urlpatterns += location_router.urls
