from django.shortcuts import render
from .models import Post
from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "homepage.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = "post_list.html"


class PostDetails(generic.DetailView):
    model = Post
    template_name = "post_details.html"


class DraftPostList(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-date_created')
    template_name = "posts_draft_list.html"
