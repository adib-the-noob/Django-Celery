from django.urls import path
from .views import say_hello
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('', say_hello, name='home'),
] 

urlpatterns += router.urls