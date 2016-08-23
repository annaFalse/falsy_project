from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Tags, Blogs



class indexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_blog'
    def get_queryset(self):
        return Blogs.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Blogs
    template_name = 'blogs/detail.html'


def tag(blog_id):
    tags = Blogs.objects.get(id=blog_id)
    list_tags = [t.tag for t in tags.tags.all()]
    return list_tags