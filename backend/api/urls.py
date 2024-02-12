from django.urls import include, path

from .views import BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', BlogListCreateAPIView.as_view()),
    path('posts/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
