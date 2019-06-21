from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.


def blog_title(requsest):
    blogs = BlogArticles.objects.all()
    return  render(requsest, "blog/titles.html", {"blogs":blogs})


def blog_article(request, article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)  #避免无id时报错。返回4040页面
    pub = article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub})