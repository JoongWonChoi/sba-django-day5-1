from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Users

def index(req):
    return HttpResponse("Welcome to my site make new version")
def register(req):
    users = Users.objects.order_by('username')
    return render(req, 'register.html', {'users':users})

def mysite(req):
    if req.method == "POST":
        post = req.POST
        data = {
                'first': post.get('first'),
                'second': post.get('second')
                }
        return render(req, "receive.html", data)
    else:
        return render(req,"mysite.html")

def formtest(req):
    if req.method != "POST":
        return render(req, "formtest.html")
    else:
        post = req.POST
        data = { 
                'name': post.get('name'),
                'gender' : post.get('gender'),
                'birthday' : post.get('birthday')

                }
        if post.get('name')=='조소명':
            return render(req, "birthday.html")
        return render(req, "formtest2.html",data)






# Create your views here.
