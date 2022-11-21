from django.urls import path

from . import views


urlpatterns = [
    path('forum/', views.ForumListCreateView.as_view()),
    path('news/<int:pk>/', views.ForumRetrieveUpdateDeleteView.as_view()),
    path('forum/<int:forum_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('forum/<int:forum_id>/comments/<int:pk>/', views.CommentRetrieveDestroyUpdateAPIView.as_view()),

]