from django.shortcuts import render, HttpResponse
from django.template.loader import get_template


# Create your views here.

def index(request):
    '''

    # (1)获取模板文件
    template = get_template("index.html")

    # (2)获取数据
    context = {"name": "admin"}

    # (3)渲染
    html = template.render(context, request)
    print("---", html)
    return HttpResponse(html)

    '''

    return render(request, "index.html", {"name": "admin"})  # 一步完成
