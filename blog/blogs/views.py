from django.shortcuts import get_object_or_404, render

from .models import Blogs



def index(request):
    latest_blog = Blogs.objects.order_by('-blog_date')[:5]
    context = {'latest_blog': latest_blog}
    return render(request, 'blogs/index.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})


def tag(blog_id):
    tags = Blogs.objects.get(id=blog_id)
    list_tags = [t.tag for t in tags.tags.all()]
    return list_tags