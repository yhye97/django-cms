from django.contrib import admin
from post.models import Category, Post, Comment 
from post.forms import *
from django.template.response import TemplateResponse
from django.conf.urls import url
from post.filters import CreatedDateFilter
from django.contrib.admin import AdminSite

class CommentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Comment._meta.fields]

class CommentAdminSite(AdminSite): 
    site_header = 'Comment administration' 

comment_admin = CommentAdminSite(name='comment_admin') 
comment_admin.register(Comment, CommentAdmin)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    form = MyPostAdminForm
    list_per_page = 10
    list_display = ('id', 'title', 'member', 'is_deleted', 'created_at', )
    list_editable = ('is_deleted', )
    list_filter = (CreatedDateFilter, 'member__permission', 'category__name', 'is_deleted', )
    empty_value_display = '-'

    fieldsets = (
        ('기본 정보', {
            'fields': (('member', 'category',), )
        }),
        ('제목 및 내용', {
        'fields': ('title', 'subtitle', 'content',)
        }),
        ('삭제', {
        'fields': ('is_deleted', 'deleted_at', )
        })
    )


    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        post_urls = [
            url(r'^status/$', self.admin_site.admin_view(self.post_status_view))
        ]
        return post_urls + urls

    def post_status_view(self, request):
        context = dict(
           self.admin_site.each_context(request), 
            posts=Post.objects.all(), 
         
        )
        return TemplateResponse(request, "admin/post_status.html", context)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
