from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/")
def posts(request):
    return render(request, "post_list.html")


def myPosts(request):
    return render(request, "myposts.html")


def postDetails(request, id):
    return render(request, "details.html")


def createpost(request):
    return render(request, "create.html")
