from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
# Create your views here.
from .models import Articles
from  .models import Comment


def index(request):
    return  render(request,'news/Home.html')

def viewList(request):
    list_news= Articles.objects.all()
    ct={"dstin":list_news}
    return  render(request,'news/newslist.html',ct)

def contentN(request,art_id):
    ctn=Articles.objects.get(pk=art_id)
    return  render(request,'news/viewContent.html',{"nd":ctn})


def indexdemo(request):
    return render(request,'news/Demo.html')
def viewLastestNews(request):
    list_dmnews=Articles.objects.all()
    dmct={"lnews":list_dmnews}
    return render(request,'news/demoviewlistnews.html',dmct)
def viewContentdemo(request,art_id):
    dmct1=Articles.objects.get(pk=art_id)
    return  render(request,'news/demoviewContent.html',{"nd1":dmct1})