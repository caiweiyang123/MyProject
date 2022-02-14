from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import redirect
from myapp.models import Users


# Create your views here.

def index(request):
    # print(reverse("add"))  # reverse通过路由名称反向生成url请求地址
    # print(reverse("index"))
    # print(reverse("find3", args=(100, "lisi")))
    # return redirect(reverse("find3", args=(100, "lisi"))) # 执行浏览器重定向
    # 执行Models的操作

    # 添加操作
    # ob = Users() # 实例化一个新对象（空对象）
    # ob.name = "李四"
    # ob.age = 19
    # ob.phone = "132132234"
    # ob.save()  # 新对象就是添加，已存在对象则是修改

    # 删除操作
    # mod = Users.objects  # 获取users的models对象
    # user = mod.get(id=4)  # 获取id值为3的用户数据信息
    # print(user.name)
    # user.delete()  # 执行删除操作

    # 修改操作
    # ob = Users.objects.get(id=5)
    # # print(ob.name)
    # ob.name = "小刘"
    # ob.age = 26
    # ob.save()

    # 数据的查询
    mod = Users.objects # 获取Users模型的操作对象

    return HttpResponse("首页!")



def add(request):
    return HttpResponse("add.......")


def find(request, sid=0, name=""):
    return HttpResponse(f"find.........{sid}{name}")


def update(request):
    # return HttpResponse("update.......")
    raise Http404("修改页面不存在")


def fun(request, yy, mm):
    return HttpResponse("参数信息：%s年%s月" % (yy, mm))
