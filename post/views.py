from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from post.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


#class ProfileView(DetailView):
#    template_name = 'posts/profile_detail.html'

#    @login_required
#    def get(self, request):
#        user_profile = Profile.objects.get(user=request.user)
#
#        return render(request, self.template_name, {'user_profile': user_profile})




class PostList(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/posts_list.html"

class PostsView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.task = self.get_object()
            post.save()
            return redirect('post', pk=post.post.pk)
        else:
            pass


class PostsCreateView(CreateView):
    model = Post
    template_name = "posts/post_form.html"
    form_class = PostForm
    success_url = reverse_lazy("post-list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("post-list")

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    template_name = "posts/post_delete.html"
    
class CustomLoginView(LoginView):
    template_name = "posts/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "login"


class RegisterView(CreateView):
    template_name = "posts/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("login"))