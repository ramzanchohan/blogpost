from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, contact, Comment, Reply
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user_authentication.models import UserProfile
from user_authentication.views import userlogin, logout
from user_authentication.urls import urlpatterns


# Create your views here.


def index(request):
    all_posts = BlogPost.objects.all()
    created_at = timezone.now()  # Set the current timestamp
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page', 1)
    print(page_number)
    page_obj = paginator.get_page(page_number)
    context = {"allposts": page_obj}  # Use 'page_obj' instead of 'all_posts'
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def contact_us(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        user_message = request.POST.get('message')
        print(user_name, user_email, user_phone, user_message)
        contact_view = contact(name=user_name, email=user_email, phone=user_phone, message=user_message)
        contact_view.save()
    return render(request, 'blog/contact_us.html')


def about_us(request):
    return render(request, 'blog/about_us.html')




@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')

        # Perform validation on the form data if necessary

        blog_post = get_object_or_404(BlogPost, pk=post_id)
        comment = Comment.objects.create(blog_post=blog_post, name=request.user.username, content=content)
        comment.save()

    return redirect('detail', post_id=post_id)


@login_required
def add_reply(request, comment_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = get_object_or_404(Comment, pk=comment_id)
        reply = Reply.objects.create(comment=comment, name=request.user.username, content=content)
        reply.save()

    return redirect('detail', post_id=comment.blog_post.id)
