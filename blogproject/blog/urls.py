from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
	path('post/<int:pk>/', views.detail, name='detail'),
	path('archives/<year>/(<month>/', views.archives, name='archives'),
	path('category/<int:pk>/', views.category, name='category'),
	path('', views.index, name='index'),
]
#path的参数中,一为路由地址,二为处理函数,三为处理函数名