from django.urls import include, path
from .views import (BlogListCreateAPIView,
                    BlogRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('posts/', BlogListCreateAPIView.as_view()),
    path('posts/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view()),
]
