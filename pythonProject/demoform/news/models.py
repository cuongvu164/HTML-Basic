from django.db import models
from datetime import  timezone
from django.contrib.admin import  widgets as admin_widgets
from tinymce import widgets as tinymce_widgets
from tinymce.models import HTMLField
# Create your models here.
class Users(models.Model):
    user_id =models.IntegerField()
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=70)

class Categories(models.Model):
    ctg_id=models.IntegerField()
    ctg_name=models.CharField(max_length=20)

class Articles(models.Model):
    art_id=models.IntegerField()
    art_name=models.CharField(max_length=70)
    art_image=models.ImageField(upload_to='Images/')
    art_summary=models.CharField(max_length=255)
    art_content=HTMLField()
    art_create_time=models.DateTimeField(auto_now_add=timezone)

class Comment(models.Model):
    cmt_pk=models.ForeignKey(Articles,on_delete=models.CASCADE)
    cmt_id=models.IntegerField()
    cmt_content=models.CharField(max_length=200)
    cmt_name=models.CharField(max_length=30)







