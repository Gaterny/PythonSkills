#### 单例模式（Singleton Pattern）：是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
#### 实现单例模式的几种方法：

1.使用模块：python的模块就是天然的单例模式，模块在第一次被导入时，会生成.pyc文件，第二次被导入时就会直接加载.pyc文件，而不会再次执行模块代码
```
#singleton.py
class Singleton:
	def foo(self):
		pass
my_singleton = Singleton()

-----------调用------------
from singleton import my_singleton
mysingleton.foo()
```

2.重构__new__方法:将类的实例与一个类变量关联起来，如果cls._instance为None，则创建实例，否则直接返回cls._instance
```
class Singleton(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance
		
class Foo(Singleton):
	pass
foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)    # True		
```


3.使用装饰器：创建一个字典instances,缓存了所有单例类，只要单例不存在则创建，已经存在直接返回该实例对象
```
def singleton(cls):
	instances = {}
	def wrapper(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
		
@singleton
class Foo(object):
	pass
	
foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)    # True
```


4.使用元类:类对象在创建实例对象时一定会调用__call__方法，因此只要保证调用__call__方法时只创建一个实例即可。
```
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
class MyClass(object):
    __metaclass__ = Singleton

# Python3
class MyClass(metaclass=Singleton):
    pass
```
