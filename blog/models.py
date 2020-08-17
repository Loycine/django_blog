from django.db import models

# Category

# Create your models here.

from mdeditor.fields import MDTextField

class Category(models.Model):
    '''
    分类
    '''
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, verbose_name='状态', default=STATUS_NORMAL)

    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '分类'


    def __str__(self):
        return self.name
    


class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    文章
    '''

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2

    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿')
    )

    title = models.CharField(max_length=255, verbose_name= '标题')
    desc = models.CharField(max_length=1024, verbose_name= '摘要')
    content = MDTextField(verbose_name= '正文')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, verbose_name='状态', default=STATUS_NORMAL)
    Category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        # 根据文章id降序排列
        ordering = ['-id']

    def __str__(self):
        return self.title