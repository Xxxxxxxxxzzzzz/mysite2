from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.blog_title), #第一个参数为空，即访问应用的根：127.0.0.1:8000/blog。第二个参数为响应这个请求的函数。
    path('<int:article_id>/', views.blog_article),
]