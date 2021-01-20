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

def git(req):
    return HttpResponse("visualcodetest-git")


def gugu(req):
    num = req.GET.get('num','')
    print(type(num))
    return HttpResponse(f"gugu : <br> {num_gugu(num)}")

def num_gugu(num):
    str = ""
    _num_ = int(num)
    for i in range (1,10):
        str += f"{_num_} x {i} = {_num_*i} <br>"
        
    return str





# Create your views here.
