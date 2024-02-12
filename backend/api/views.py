from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from blogs.models import Blog

from .permissions import IsOwnerOrAdmin
from .serializers import BlogSerializer


class BlogListCreateAPIView(APIView):
    """Чтение и создание постов."""

    def get(self, request):
        posts = Blog.objects.all()
        serializer = BlogSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogRetrieveUpdateDestroyAPIView(APIView):
    """Чтение, изменение и удаление постов по id."""

    permission_classes = [IsOwnerOrAdmin]

    def get_object(self, pk):
        return get_object_or_404(Blog, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BlogSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        self.check_object_permissions(request, self.get_object(pk))
        post = self.get_object(pk)
        serializer = BlogSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_object_permissions(request, self.get_object(pk))
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
