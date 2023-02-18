
from ads import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from homework_27 import settings

# шаблоны URL-адресов
urlpatterns = [
    path('cat/', views.CategoryListView.as_view(), name="category_list"),
    path('cat/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category_update"),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name="category_delete"),

    path('ad/', views.AdvertisementListView.as_view(), name="ad_list"),
    path('ad/create/', views.AdvertisementCreateView.as_view(), name="ad_create"),
    path('ad/<int:pk>/', views.AdvertisementDetailView.as_view(), name="ad_detail"),
    path('ad/<int:pk>/update/', views.AdvertisementUpdateView.as_view(), name="ad_update"),
    path('ad/<int:pk>/delete/', views.AdvertisementDeleteView.as_view(), name="ad_delete"),
    path('ad/<int:pk>/upload_image/', views.AdvertisementImageUpdateView.as_view(), name="ad_update_image"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
