from django.urls import path
from post import views

urlpatterns = [
    path("", views.PostList.as_view(), name='post-list'),
    path("<int:pk>", views.PostsView.as_view(), name='post-detail'),
    path("<int:pk>/updateHL/", views.PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/deleteHL/", views.PostDeleteView.as_view(), name="post-delete"),
    path("post_createHL/", views.PostsCreateView.as_view(), name="post-create"),
    path("loginHL/", views.CustomLoginView.as_view(), name="login"),
    path("logoutHL/", views.CustomLogoutView.as_view(), name="logout"),
    path("registerHL/", views.RegisterView.as_view(), name="register"),
]