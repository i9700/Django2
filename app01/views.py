from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import get_template
from datetime import datetime
from django.urls import reverse


# Create your views here.
class Book(object):
    def __init__(self, title, price, publish):
        self.title = title
        self.price = price
        self.publish = publish

    def __str__(self):
        return self.title


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
    name = "root"
    age = 22
    score = 85
    is_married = False

    book_list = ["三国演义", "水浒传", "西游记", "金瓶梅"]

    admin = {"name": "tao", "age": 18}

    book01 = Book("三体", 99, "苹果出版社")
    book02 = Book("飘", 199, "苹果出版社")
    book03 = Book("乱世佳人", 299, "西瓜出版社")
    book04 = Book("放风筝的人", 99, "苹果出版社")
    books = [book01, book02, book03, book04]
    books2 = []
    now_time = datetime.now()
    file_size = 12364556
    content = "i am ok find..."

    link = "<a href ='http://www.baidu.com'>baidu</a>"
    comment = "<script>alert(123)</script>"
    my_tel = "18779114639"
    return render(request, "index.html", locals())  # 一步完成


# 反向解析
def login(request):
    path = reverse("ind")
    return redirect(path)


def order(request):
    order_list = ["订单1", "订单2", "订单3"]
    print("反向解析:", reverse("ind"))
    return render(request, "order.html", {"order_list": order_list})
