from django.urls import path
from .views import PostListView, PostDetailView, SignupView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignupView.as_view(), name='signup'),
]