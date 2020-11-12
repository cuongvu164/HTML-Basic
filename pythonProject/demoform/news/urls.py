from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name="index"),
    path('list',views.viewList,name="list_news"),
    path('list/<int:art_id>',views.contentN,name="view_content"),
    path('demo',views.indexdemo,name="indexdemo"),
    path('demo/list',views.viewLastestNews,name="dml"),
    path('demo/list/<int:art_id>',views.viewContentdemo,name="dmct"),
]