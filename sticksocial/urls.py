from django.urls import path
from .views import PostListView,PostDetailView, PostDeleteView, CommentDeleteView, PostEditView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDisLike

urlpatterns = [
    path('', PostListView.as_view(), name='POST_LIST'),
    path('post/<int:pk>', PostDetailView.as_view(),name='POST_DETAIL'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='POST_DELETE'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='COMMENT_DELETE'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDisLike.as_view(), name='dislike'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='POST_EDIT'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='PROFILE_EDIT'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
]
