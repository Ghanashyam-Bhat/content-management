from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import models
from authentication import models as userModel
from datetime import datetime


# Create your views here.
@login_required(login_url="/auth/")
def posts(request):
    return render(request, "post_list.html")


def myPosts(request):
    return render(request, "myposts.html")


def postDetails(request, id):
    return render(request, "details.html")


def createpost(request, id=None):
    title = ""
    subheading = ""
    content = ""
    image = None
    updated = None
    user = userModel.user.objects.get(id=request.user)
    post_url = "/post/new/"
    if request.method == "GET":
        if id != None:
            post = models.post.objects.get(id=id)
            title = post.title
            subheading = post.subheading
            content = post.content
            post_url = f"/post/edit/{id}"
        return render(
            request,
            "create.html",
            context={
                "title": title,
                "subheading": subheading,
                "content": content,
                "post_url": post_url,
            },
        )
    elif request.method == "POST":
        if id == None:
            # New post
            try:
                image = request.FILES.get("img")
            except Exception as e:
                print("No image data")
            title = request.POST.get("title")
            subheading = request.POST.get("subheading")
            content = request.POST.get("content")
            updated = datetime.now()
            new = models.post(
                title=title,
                subheading=subheading,
                content=content,
                image=image,
                updated=updated,
                user=user,
            )
            new.save()
        else:
            # Update post
            post = models.post.objects.get(id=id)
            try:
                image = request.FILES.get("img")
                post.image = image
            except Exception as e:
                print("No image data")
            title = request.POST.get("title")
            subheading = request.POST.get("subheading")
            content = request.POST.get("content")
            updated = datetime.now()

            post.title = title
            post.subheading = subheading
            post.content = content
            post.updated = updated
            post.save()
        return redirect("/post/personal/")
