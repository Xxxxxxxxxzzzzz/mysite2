from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.


#在视图函数中要处理前端提交的数据，并支持前端的显示请求，视图函数必须使用request作为第一个函数。request:Httprequest
def blog_title(requsest):
    blogs = BlogArticles.objects.all()  #将BlogArticles类的所有参数的实例赋值给blogs
    return render(requsest, "blog/titles.html", {"blogs": blogs})  #将"blogs"（数据）传送给titles.html（模板）


def blog_article(request, article_id): #article_id参数目的是获取titles.html中的超链接title.id（每篇文章的id）
    #article = BlogArticles.objects.get(id=article_id)  读取id值是article_id的记录
    article = get_object_or_404(BlogArticles, id=article_id)  #避免无id时报错。返回4040页面
    return render(request, "blog/content.html", {"article": article})  #将"article"传送给content.html
