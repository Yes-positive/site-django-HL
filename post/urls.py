from django.urls import path
from post import views

urlpatterns = [
    path("postHL/<int:pk>", views.PostsView.as_view(), name='task-post'),
]