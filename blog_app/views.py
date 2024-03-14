from typing import Any
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.models import Post, Comment
from blog_app.forms import PostForm, CommentForm

# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    template_name = "home.html"
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = "blog_app/post_detail.html"
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = "blog_app/post_detail.html"
    form_class = PostForm
    model = Post
    
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "post_draft.html"
    login_url = '/login/'
    redirect_field_name = "blog_app/home.html"
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
    
@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

# Comment views here

@login_required
def add_comments(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog_app/comment_form.html',context={'form':form})

@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk =  comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
