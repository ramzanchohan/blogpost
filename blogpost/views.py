from django.core.paginator import Paginator
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
    paginator = Paginator(all_posts, 12)
    page_number = request.GET.get('page', 1)
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

# blog/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Comment, Reply
# from .forms import CommentForm, ReplyForm
# from django.contrib.auth.decorators import login_required
#
#
# class Post:
#     pass
#
#
# def add_comment(request, post_id):
#     # Assume you have a blog post model named "Post"
#     # Replace "Post" with the actual model name if different
#     post = get_object_or_404(Post, id=post_id)
#     comments = Comment.objects.filter(post=post)
#     comment_form = CommentForm()
#
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.user = request.user
#             comment.save()
#             return redirect('detail', post_id=post_id)
#
#     return render(request, 'blog/detail.html', {
#         'post': post,
#         'comments': comments,
#         'comment_form': comment_form,
#     })
#
# @login_required
# def add_reply(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)
#     if request.method == 'POST':
#         reply_form = ReplyForm(request.POST)
#         if reply_form.is_valid():
#             reply = reply_form.save(commit=False)
#             reply.comment = comment
#             reply.user = request.user
#             reply.save()
#     return redirect('detail', post_id=comment.post.id)
