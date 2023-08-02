from django.db import models
from datetime import date


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    pub_date = models.DateField(default=date.today())
    image = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title


class contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from' ' ' + self.name


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)