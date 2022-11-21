from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from .models import Forum, Comment
from .permissions import BasePermission
from .serializers import ForumSerializers, CommentSerializer
from rest_framework.response import Response


class ForumListCreateView(ListCreateAPIView):
    """
    Forum API endpoint to get list of blogs and create forum
    """

    queryset = Forum.objects.all()
    serializer_class = ForumSerializers
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]

    def post(self, request, *args, **kwargs):
        serializer = ForumSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForumRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    Forum API endpoint to retrieve, update and delete forum
    """

    queryset = Forum.objects.all()
    serializer_class = ForumSerializers
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]


class CommentListCreateAPIView(ListCreateAPIView):
    """
    Forum API endpoint to get list of blogs and create forum
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(forum_id=self.kwargs['forum_id'])

    def perform_create(self, serializer):
        try:
            serializer.save(
                user=self.request.user,
                forum=get_object_or_404(Forum, id=self.kwargs['forum_id'])
            )
        except ValueError:
            serializer.save(
                forum=get_object_or_404(Forum, id=self.kwargs['forum_id'])
            )


class CommentRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """
    Forum API endpoint to retrieve, update and delete forum
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]
