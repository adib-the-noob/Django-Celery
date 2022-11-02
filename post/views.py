from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .tasks import notify_cutomers
from .models import Post
# Create your views here.

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



def say_hello(request):
    notify_cutomers.delay("Hello World")
    return render(request, 'index.html', {})