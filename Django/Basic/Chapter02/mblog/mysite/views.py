from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime

# Create your views here.


def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)

        print(post.title)

        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def homepage(request):
    posts = Post.objects.all()

    # post_lists = list()

    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}: ".format(str(count)) + str(post) + "<hr>")
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")

    # return HttpResponse(post_lists)

    now = datetime.now()

    return render(request, "index.html", locals())
