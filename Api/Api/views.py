from django.shortcuts import render
from rest_framework import mixins,viewsets,generics,permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from .permissions import IsAdminOrReadOnly

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[IsAdminOrReadOnly]
    

