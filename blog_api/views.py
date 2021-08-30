from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# View Level Permission(customized)
class PostUserWriterPermission(BasePermission):
    message = 'Editing posts is restriced to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        return obj.author == request.user

# ModelViewSet


# class PostList(viewsets.ModelViewSet):
#     #permission_classes = [PostUserWriterPermission]
#     serializer_class = PostSerializer
#     queryset = Post.postobjects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()

class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    print("detail")

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# # Using ViewSet
# class PostList(viewsets.ViewSet):
#     #permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):  # individual item
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)


# class PostListDetailfilter(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']
'''

CreateAPIView
Used for create-only endpoints.

Provides a post method handler.

Extends: GenericAPIView, CreateModelMixin

ListAPIView
Used for read-only endpoints to represent a collection of model instances.

Provides a get method handler.

Extends: GenericAPIView, ListModelMixin

RetrieveAPIView
Used for read-only endpoints to represent a single model instance.

Provides a get method handler.

Extends: GenericAPIView, RetrieveModelMixin

DestroyAPIView
Used for delete-only endpoints for a single model instance.

Provides a delete method handler.

Extends: GenericAPIView, DestroyModelMixin

UpdateAPIView
Used for update-only endpoints for a single model instance.

Provides put and patch method handlers.

Extends: GenericAPIView, UpdateModelMixin

ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.

Provides get and post method handlers.

Extends: GenericAPIView, ListModelMixin, CreateModelMixin

RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.

Provides get, put and patch method handlers.

Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin

RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.

Provides get and delete method handlers.

Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin

RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.

Provides get, put, patch and delete method handlers.

Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
'''
