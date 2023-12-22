from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        if (serializer := PostSerializer(data=request.data)).is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericPostApiView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
