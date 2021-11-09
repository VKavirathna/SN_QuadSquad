from django.urls import path
from .views import PostListView,PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='POST_LIST'),
    path('post/<int:pk>', PostDetailView.as_view(),name='POST_DETAIL'),
]