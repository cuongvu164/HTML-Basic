from django.contrib import admin
from .models import Users,Articles,Categories,Comment
# Register your models here.
admin.site.register(Users),
admin.site.register(Categories),
admin.site.register(Articles),
admin.site.register(Comment),
