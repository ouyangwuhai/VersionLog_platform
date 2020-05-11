from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.

# def say_hello(request):
#     name = request.GET.get("name","")
#     if name == "":
#         return HttpResponse("请输入name参数")
#     else:
#         #return HttpResponse("hello "+ name)
#         return render(request,"index.html",{"name":name})

def index(request):
    if request.method == "GET":
        return render(request,"index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"errmsg": "用户名或密码为空"})
        else:
            user = auth.authenticate(username=username,password=password)
            if user == None:
                return render(request, "index.html", {"errmsg": "用户名或密码错误"})
            else:
                # auth.login(request,user) #记录用户登入状态
                # return HttpResponse("恭喜你，登入成功")
                return HttpResponseRedirect("/manage/")
def manage(request):
    return render(request,"manage.html")

def ceshit(request):
    pass

def ceshiaaa(request):
    pass

def ceshibbb(request):
    pass


def cesthi2(request):
    print("hello world!")


