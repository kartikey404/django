from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    model = Post
    template_name = 'devapp/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'devapp/create_post.html'
    success_url = reverse_lazy('home')  # redirect after success

    def form_valid(self, form):
        form.instance.author = self.request.user  # ← Set the author
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'devapp/update_post.html'
    success_url = reverse_lazy('home')

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'devapp/delete_post.html'
    success_url = reverse_lazy('home')
