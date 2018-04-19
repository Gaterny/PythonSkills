from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#分类功能,实际是创建category数据库表,name是列名
class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=100)  #存储较短的字符使用CharField
	def __str__(self):
		return self.name

#标签
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

#文章
class Post(models.Model):
	title = models.CharField(max_length=100)  #文章标题

	body = models.TextField()  #文章正文,使用TextField

	#创建和最后修改时间
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	#摘要,指定blank之后,参数可以为空
	excerpt = models.CharField(max_length=250, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) #一对多的关联关系
	tags = models.ManyToManyField(Tag, blank=True) #多对多的关系,文章可以没有标签

	author = models.ForeignKey(User, on_delete=models.CASCADE)  #一对多的关系,一篇文章只有一个作者,一个作者可以有很多文章.
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})