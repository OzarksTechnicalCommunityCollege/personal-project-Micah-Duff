from django.shortcuts import get_object_or_404, render
from .forms import EmailPostForm
from .models import Post
from django.http import Http404
from django.core.mail import send_mail

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'comic/post/list.html',
        {'posts': posts}
    )
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
    Post,
    status = Post.Status.PUBLISHED,
    slug=post,
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render (
        request,
        'comic/post/detail.html',
        {'post' : post},
    )

# I really liked the idea of email sharing, so i pretty much followed the book and implemented the feature as shown in chapter 2
def comic_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
                )
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {post.title}"
                )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['message']}"
                )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        'comic/post/share.html',
        {
            'post':post,
            'form':form
        }
    )
    