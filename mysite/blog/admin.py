#django自带图形化管理界面，该应用的后台管理系统配置
from django.contrib import admin
from .models import BlogArticles  #将BlogArticles类引入到当前环境

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")  #过滤器：以publish、author分类
    search_fields = ('title', "body")  #搜索引擎：以title、body内容搜索
    raw_id_fields = ("author",)  #将作者对应指向id
    date_hierarchy = "publish"  #以日，月，年，所有检索
    ordering = ['-publish', 'author']  #？


admin.site.register(BlogArticles, BlogArticlesAdmin)  #将该BlogArticles类注册到admin中