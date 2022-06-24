from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class BlogDeleteView(PostDeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")