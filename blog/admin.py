from django.contrib import admin
from .models import Post
from django.http import HttpResponse

from django.contrib.admin import AdminSite

admin.site.register(Post)



class MyAdminSite(AdminSite):

     def get_urls(self):
         from django.conf.urls import url
         urls = super(MyAdminSite, self).get_urls()
         urls += [
             url(r'^my_view/$', self.admin_view(self.my_view))
         ]
         return urls

     def my_view(self, request):
         return HttpResponse("Hello!")

admin_site = MyAdminSite()