from django.urls import path
from .views import PostListView,PostDetailView, PostDeleteView, CommentDeleteView, PostEditView



urlpatterns = [
    path('', PostListView.as_view(), name='POST_LIST'),
    path('post/<int:pk>', PostDetailView.as_view(),name='POST_DETAIL'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='POST_DELETE'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='COMMENT_DELETE'),
path('post/edit/<int:pk>/', PostEditView.as_view(), name='POST_EDIT'),
]