from django.shortcuts import render, get_object_or_404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)

from .models import Post

def post_list(request):
    post_list = Post.published.all()

    # Pagination with 3 posts per page

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
        
    except PageNotAnInteger:
        # If page_number is not an integer, deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # If page_number is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post_list.html',
                  {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post)
    
    return render(request,
                  'blog/post_detail.html',
                  {'post': post})
