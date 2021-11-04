from django.urls import path
from landing1.views import Index

urlpatterns = [
    path('', Index.as_view(), name='INDEX'),
]
