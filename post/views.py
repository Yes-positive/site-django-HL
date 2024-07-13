from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .models import Post
from post.forms import PostForm
# Create your views here.



class PostsView(CreateView):
    model = Post
    template_name = 'posts/posts.html'

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.task = self.get_object()
            post.save()
            return redirect('task-post', pk=post.post.pk)
        else:
            pass