from django.urls import path
from .views import PostListView,PostDetailView, PostDeleteView, CommentDeleteView, PostEditView, ProfileView, ProfileEditView



urlpatterns = [
    path('', PostListView.as_view(), name='POST_LIST'),
    path('post/<int:pk>', PostDetailView.as_view(),name='POST_DETAIL'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='POST_DELETE'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='COMMENT_DELETE'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='POST_EDIT'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='PROFILE_EDIT'),
]