from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#数据模型类：使用ORM框架，类似于MVC结构中的Models
#Django中的所有数据模型类都继承自django.db.models.Model类
#通常一个Model对应数据库的一张数据表，以类的形式表现，包含一些基本(属性)字段以及数据的一些行为
#ORM实现了对象和数据库之间的映射，隐藏了数据访问的细节，不需要编写SQL语句


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)  #字段title属性为CharField()类型，并且以参数max_length=300的形式说明字段的最大数量
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  #通过字段author规定了博客文章和用户之间的关系—一个用户对应多篇文章，ForeignKey()就反映了“一对多”（或“多对一”）的关系。
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
            return self.title
