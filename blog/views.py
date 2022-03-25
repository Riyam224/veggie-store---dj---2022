from typing import List
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from django.http import HttpResponse
from .models import Post , Category
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q




class PostList(ListView):
    model = Post
    template_name = 'blog/postList.html'

    def get_queryset(self):
        name = self.request.GET.get('q' , '')
        object_list = Post.objects.filter(
            Q(title__icontains=name) |
            Q(description__icontains=name)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['tags']  = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    
    

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'


    def get_queryset(self):
        name = self.request.GET.get('q' , '')
        object_list = Post.objects.filter(
            Q(title__icontains=name) |
            Q(description__icontains=name)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['tags']  = Tag.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    