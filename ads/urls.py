
from rest_framework import routers
from ads import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from homework_27 import settings
from ads.views import AdViewSet

router = routers.SimpleRouter()
router.register("ad", AdViewSet)
urlpatterns = [
    path('cat/', views.CategoryListView.as_view(), name="category_list"),
    path('cat/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category_update"),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name="category_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
