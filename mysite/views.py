from django.shortcuts import render,redirect
#from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime

def showpost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html',locals())
    except:
        return redirect('/')
    
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,"index.html",locals())
#    post_lists = list()
#    for count, post in  enumerate(posts):
#        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
#        post_lists.append("<small>" + str(post.body) +"</small><br><br>")
#    return HttpResponse(post_lists)


