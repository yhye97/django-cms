from django.db import models
from member.models import Member


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField('카테고리 이름', max_length=20)

    def  __str__(self):
        return self.name

class Post(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자1', on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, verbose_name='카테고리', on_delete=models.CASCADE) 
    title = models.CharField('제목', max_length=255)
    subtitle = models.CharField('부제목', max_length=255, default="")  
    content = models.TextField('내용') 
    is_deleted = models.BooleanField('삭제된 글', default=False) 
    deleted_at = models.DateTimeField('삭제일시', default=None, null=True)
    created_at = models.DateTimeField('작성일', auto_now_add=True) 
 

class Comment(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자', on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, verbose_name='원본글', on_delete=models.CASCADE)
    content = models.TextField() 
    is_blocked = models.BooleanField('노출 제한', default=False)
    
 