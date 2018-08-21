### 为了理解yield的工作原理，首先需要明白生成器以及可迭代对象是什么

> **可迭代对象**

当你创建一个列表时，你可以从列表中一个接一个的读取元素，这种一个接一个读取元素叫做迭代。
```
>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
```
mylist就是可迭代对象，当你使用列表解析式时，它既是列表也是可迭代对象。
```
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
```
Everything you can use "for... in..." on is an iterable; lists, strings, files...

These iterables are handy because you can read them as much as you wish, but you store all the values in memory and this is not always what you want when you have a lot of values.

Generators
> **生成器**

Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
生成器也是迭代器。生成器不是存储所有的变量在内存中，而是在遍历时动态的生成，且只能被迭代一次
```
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```
当你再次执行'''for i in mygenerator'''时，会返回none，因为生成器只能被迭代一次
It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

> **Yield**

yield功能与return类似，不同的是，yield返回生成器
```
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```
Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

当你调用函数时，函数体中的代码并没有运行，只是返回了一个生成器对象。只有在你调用for语句时才会从生成器中取值。

tips:当使用for从生成器中迭代数据时，函数会运行直到遇到yield返回值然后停止，再一次运行会从上次停止的位置接着运行。直到所有值都被返回

> **return与yield的区别**

example:
```
def func(n):
    for i in range(n):
        return i
        
func(3)
0
```

```
def func(n):
    for i in range(n):
        yield i
        
for i in func(3):
    print(i)
    
0
1
2
```
return只返回其中一个，yield返回一个包含所有元素的生成器。
