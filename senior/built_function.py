"""内置函数"""
abs()  # 返回数字的绝对值
# abs(x)  # x : 数值表达式，可以是整数，浮点数，复数  # abs(-45)

dict()  # 用于创建一个字典  # dict()  创建空字典
# class dict(**kwarg)  # **kwarg：关键字  # dict(a='a', b='b', t='t')  传入关键字
# class dict(mapping, **kwarg)  # mapping：元素的容器  # dict(zip(['one', 'two', 'three'], [1, 2, 3]))  映射函数方式来构造字典
# class dict(iterable, **kwarg)  # iterable：可迭代对象  # dict([('one', 1), ('two', 2), ('three', 3)])  可迭代对象方式来构造字典

help()  # 用于查看函数和模块的详细说明
# help([object])  # object：对象  # help('sys')

min()  # 返回给定参数的最小值，参数可以是序列
# min(x, y, z...)  # x,y,z：数值表达式  # min(-10, 10, 100)

max()  # 返回给定参数的最大值，参数可以为序列
# max(x, y, z)  # x、y、z：数值表达式  # max(-20, 10, 20)

setattr()  # 用于设置属性值，该属性不一定是存在的
# setattr(object, name, value)  # object：对象 name：字符串，对象属性 value：属性值
# 对于已存在的属性进行赋值
class A(object):
    bar = 1
a = A()
getattr(a, 'bar')  # 获取属性bar值
setattr(a, 'bar', 5)  # 设置属性bar值
# 属性不存在时，会创建一个新的属性对象，并对属性赋值
class A():
    name = 'bar'
a = A()
setattr(a, 'age', 22)

getattr()  # 用于返回一个对象属性值
# getattr(object, name[, default])  # object：对象 name：字符串，对象属性
# default：默认返回值，如果不提供该参数，在没有对应属性时，将触发AttributeError
class A():
    bar = 1
a = A()
getattr(a, 'bar')  # 获取属性bar的值
getattr(a, 'bar2')  # 属性bar2不存在，触发异常
getattr(a, 'bar2', 3)  # 属性bar2不存在，但设置了默认值

all()  # 用于判断给定的可迭代参数iterable中的所有元素是否都为TRUE，如果是返回True，否则返回False，注意：元素除了是0，空，None，False外都算True
# all(iterable)  # iterable：元组或者列表  # all(['a', 'b', 'c'])
# 注意：空元组、空列表返回值为True，这里要特别注意。

any()  # 用于判断给定的可迭代参数iterable是否全部为False，则返回False，如果有一个为True，则返回True，注意：元素除了是0，空，None，False外都算True
# all(iterable)  # iterable：元组或者列表  # any(['a', 'b', '', 'd'])
# 注意：空元组、空列表返回值为False，这里要特别注意。

dir()  # 不带参数时，返回当前范围内的变量、方法和定义的类型列表，带参数时，返回参数的属性、方法和列表
# 如果参数包含方法__dir__()，该方法将被调用，如果参数不包含__dir__()，该方法将最大限度的收集参数信息
# dir([object])  # object：对象、变量、类型  # dir() 获取当前模块的属性列表

hex()  # 用于将一个指定数字转换为16进制数
# hex(x)  # x：一个整数  # hex(10)

next()  # 返回迭代器的下一个项目
# next(iterator [, default])  # iterator：可迭代对象  default：可选，用于设置在没有下一个元素时返回默认值，
# 如果不设置，又没有下一个元素则会触发StopIteration
# # 首先获得Iterator对象：
# it = iter([1, 2, 3, 4, 5])
# # 循环：
# while True:
#     try:
#         # 获取下一个值：
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         pass

slice()  # 函数实现切片对象，主要用在切片操作函数里的参数传递
# class slice(stop)
# class slice(start, stop[, step])  # start：起始位置  stop：结束位置  step：间距
myslice = slice(5)  # 设置截取元素的切片
arr = range(10)
arr[myslice]  # 截取5个元素

divmod()  # 把除数和余数运算结果结合起来，返回一个包含商和余数的元组（a//b，a%b）
# divmod(a, b)  # a,b：数字  # divmod(7, 2)

id()  # 用于获取对象的内存地址
# id([object])  # object：对象  # a = 1  id(a)

sorted()  # 对所有可迭代的对象进行排序操作
# sorted(iterable, key=None, reverse=False)  # iterable：可迭代对象  key：主要是用来进行比较的元素，只有一个参数，
# 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序  reverse：排序规则，reverse = True 降序，
# reverse = False 升序（默认）  a = [3, 4, 1, 9] sorted(a)

ascii()  # 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数
# 使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
# ascii(object)  # object：对象  # ascii(1)

repr()  # 将对象转化为供解释器读取的形式，返回的对象是字符串格式
# repr(object)  # object：对象  # repr(1)

enumerate()  # 用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中
# enumerate(sequence, [start=0])  # sequence：一个序列、迭代器或其他支持迭代对象  start：下标起始位置
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])

input()  # 接收一个标准输入数据，返回string类型
# input([prompt])  # prompt：提示信息  # a = input("input:")  input:123  # 输入整数

oct()  # 将一个整数转换成8进制字符串
# oct(x)  # x：整数  # oct(10)

staticmethod()  # 返回函数的静态方法，该方法不强制要求传递参数，如下声明一个静态方法：
class C(object):
    @staticmethod
    def f(arg1, arg2, argN):
        ...
# 以上实例声明了静态方法f，类可以不用实例化就可以调用该方法C.f()，当然也可以实例化后调用C().f()
class C(object):
    @staticmethod
    def f():
        print('run')
C.f()  # 静态方法无需实例化
cobj = C()  # 也可以实例化后调用
cobj.f()

bin()  # 返回一个整数int或者长整数long int的二进制表示，返回一个字符串
# bin(x)  # x：int或者long int 数字  # bin(10)

eval()  # 用来执行一个字符串表达式，并返回表达式的值
# eval(expression[, globals[, locals]])  # expression：表达式  # globals：变量作用域，全局命名空间，如果被提供，
# 则必须是一个字典对象  locals：变量作用域，局部命名空间，如果被提供，可以是任何映射对象  # eval('1 + 1')

exec()  # 执行储存在字符串或文件中的python语句，相比于eval，exec可以执行更复杂的python代码
# exec(object[, globals[, locals]])  # object：必选参数，表示需要被指定的python代码，它必须是字符串或code对象，如果object是
# 一个字符串，该字符串会先被解析为一组python语句，然后在执行（除非发生语法错误），如果object是一个code对象，那么它只是被简单的执行
# globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象  locals：可选参数，表示当前局部命名
# 空间（存放局部变量），如果被提供，可以是任何映射对象，如果该参数被忽略，那么它将会取与globals相同的值
# exec("print(baidu.com)")

int()  # 用于将一个字符串或数字转换为整型
# class int(x, base=10)  # x：字符串或数字  base：进制数，默认10进制  # int('10', 8)

open()  # 用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出OSError
# 注意：使用open()方法一定要保证关闭文件对象，即调用close()方法，open()函数常用形式是接收两个参数：文件名（file）和模式（mode）
# open(file, mode='r')  # f = open('test.txt')  f.read()

str()  # 将对象转化为适于人阅读的形式，返回一个对象的string格式
# class str(object='')  # object：对象  # dict = {'aa': '1', 'bb': '22'}  str(dict)

bool()  # 用于将给定参数转换为布尔类型，如果没有参数，返回False，bool是int的子类
# class bool([x])  # x：要进行转换的参数  # bool(1)

isinstance()  # 判断一个对象是否是一个已知的类型，类似type()
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
# isinstance(object, classinfo)  # object：实例对象  classinfo:可以是直接或间接类名、基本类型或者由它们组成的元组
# a = 1  isinstance(a, int)

type()  # 如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象
# type(object)
# type(name, bases, dict)  # name：类的名称  bases：基类的元组  dict：字典，类内定义的命名空间变量
# 一个参数
type(1)
# 三个参数
class X(object):
    a = 1
X = type('X',(object,), dict(a=1))  # 产生一个新的类型X

ord()  # ord()函数是chr()函数（对于8位的ASCII字符串）的配对函数，它以一个字符串（Unicode字符）作为参数，返回对应的ASCII数值，或者Unicode数值
# ord(c)  # c：字符  # ord('a')

chr()  # 用一个整数作参数，返回一个对应的字符
# chr(i)  # i：可以是10进制也可以是16进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)  # chr(97)

sum()  # 对系列进行求和计算
# sum(iterable[, start])  # iterable：可迭代对象，如：列表、元组、集合  start：指定相加的参数，如果没有设置这个值，默认为0
sum((2, 3, 4), 1)  # 元组计算总和后再加1

bytearray()  # 返回一个新字节数组，这个数组里的元素是可变的，并且每个元素的值范围：0 <= x < 256
# class bytearray([source[, encoding[, errors]]])
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
# bytearray([1,2,3])

bytes()  # 返回一个新的bytes对象，该对象是一个0<=x<256区间内的整数不可变序列，它是bytearray的不可变版本
# class bytes([source[, encoding[, errors]]])  # bytes([1,2,3,4])

filter()  # 用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用list()来转换，该接收两个参数，
# 第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True或False，最后将返回True的元素放到新列表中
# filter(function, iterable)  # function：判断函数  iterable：可迭代对象
# 过滤出1到100中平方根是整数的数：
import math
def is_sqr(x):
    return math.sqrt(x)% 1 == 0
tmplist = filter(is_sqr, range(1, 101))
newlist = list(tmplist)
print(newlist)

issubclass()  # 用于判断参数class是否是类型参数classinfo的子类
# issubclass(class, classinfo)  # class、classinfo：类
class A:
    pass
class B(A):
    pass
print(isinstance(B, A))  # 返回True

pow()  # 返回x的y次方的值
# math模块pow()方法的语法：
# import math
# math.pow(x, y)
# 内置的pow()方法：
# pow(x,y[,z])
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float
import math  # 导入math模块
print(math.pow(100, 2))
# 使用内置，查看输出结果区别
print(math.pow(100, 2))
print(math.pow(100, 3), 10)

super()  # 用于调用父类（超类）的一个方法。super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
# 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
# super(type[, object-or-type])  # type：类 object-or-type：类，一般是self
class FooParent(object):
    def __init__(self):
        self.parent = 'I \'m the parent.'
        print('parent')

    def bar(self, message):
        print("%s from Parent"% message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild, self)首先找到FooChild的父类（就是类FooParent），然后把类B的对象FooChild转换为类FooParent的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('Hello World')

float()  # 用于将整数和字符串转换成浮点数
# class float([x])  # x：整数或字符串  # float('123')

iter()  # 用来生成迭代器
# iter(object[, sentinel])  # object：支持迭代的集合对象  sentinel：如果传递了第二个参数，则参数object必须是一个可调用的对象（如，函数），
# 此时，iter创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用object
lst = [1, 2, 3]
for i in iter(lst):
    print(i)

print()  # 用于打印输出，最常见的一个函数
# print(*objects, sep='', end='\n', file=sys.stdout)
# object：复数，表示可以一次输出多个对象，输出多个对象时，需要用逗号分隔
# sep：用来间隔多个对象，默认值是一个空格
# end：用来设定以什么结尾，默认值是换行符\n，我们可以换成其他字符串
# file：要写入的文件对象
print("www","baidu","com",sep=".")  # 设置间隔符

tuple()  # 将列表转换为元组
# tuple(seq)  # seq：要转换为元组的序列  # list1=['baidu', 'taobao']  tuple1=tuple(list1)

callable()  # 用于检查一个对象是否可调用，如果返回True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
# 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
# callable(object)  # object：对象  # callable(add)  函数返回True

format()  # python2.6开始，新增了一种格式化字符串的函数str.format()，它增强了字符串格式化的功能
# 基本语法是通过{}和：来代替以前的%，format函数可以接受无限个参数，位置可以不按顺序

len()  # 返回对象（字符、列表、元组等）长度或项目个数
# len(s)  # s：对象  str = 'run'  len(str)   字符串的长度

property()  # 作用是在新式类中返回属性值
# class property([fget[, fset[, fdel[, doc]]]])  # fget：获取属性值的函数  fset：设置属性值的函数  fdel：删除属性值函数 doc：属性描述信息

frozenset()  # 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
# class frozenset([iterable])  # iterable：可迭代的对象，比如列表、字典、元组等等
# frozenset(['r', 'u', 'n'])  # 创建不可变集合

list()  # 用于将元组或字符串转换为列表
# 注意：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中
# list(seq)  # seq：要转换为列表的元组或字符串  # str='Hello World'  list1=list(str)  print(list)

range()  # 返回一个可迭代对象（类型是对象），而不是列表类型，所以打印的时候不会打印列表
# range(stop)
# range(start, stop[, step])  # start：计数从start开始，默认是从0开始，例如range(5)等价于range(0, 5)  stop：计数到stop结束，
# 但不包括stop，例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5  step：步长，默认为1，例如：range（0， 5） 等价于 range(0, 5, 1)
# list(range(0, 30, 5))  # [0, 5, 10, 15, 20, 25]

vars()  # 返回对象object的属性和属性值的字典对象
# vars([object])  # object：对象  # print(vars())

classmethod()  # 装饰器，对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，可以来调用类的属性，类的方法，实例化对象等
class A(object):
    bar = 1
    def func1(self):
        print('foo')
    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用foo方法

A.func2()  # 不需要实例化

locals()  # 会以字典类型返回当前位置的全部局部变量
# 对于函数，方法，lambda函数，类，以及实现了__call__方法的类实例，它都返回True
def run(arg):  # 两个局部变量：arg、z
    z = 1
    print(locals())
run(4)  # 返回一个名字/值对的字典

globals()  # 以字典类型返回当前位置的全部全局变量
a = 'run'
print(globals())  # globals函数返回一个全局变量的字典，包括所有导入的变量

zip()  # 用于将可迭代的对象作为参数，将对象中对应的元素大包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存
# 我们可以使用list()转换来输出列表，如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元组解压为列表
# zip([iterable,...])  # iterable：一个或多个迭代器  # a=[1, 2, 3]  zip(a)

compile()  # 将一个字符串编译为字节代码
# compile(source, filename, mode[, flags[, dont_inherit]])  # source：字符串或者AST（Abstract Syntax Trees）对象
# filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值  mode：指定编译代码的种类，可以指定为exce、eval、single
# flags：变量作用域，局部命名空间，如果被提供，可以是任何映射对象  flags和dont_inherit是用来控制编译源码时的标志
str = '3*4+5'
a = compile(str, '', 'eval')
eval(a)

map()  # 会根据提供的函数对指定序列做映射
# 第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的新列表
# map(function, iterable,...)  # function：函数  iterable：一个或多个序列
def square(x):
    return x ** 2
map(square, [1, 2, 3, 4, 5])

reversed()  # 返回一个反转的迭代器
# reversed(seq)  # seq：要转换的序列，可以是tuple，string，list或range
seqString = 'run'
print(list(reversed(seqString)))

__import__()  # 用于动态加载类和函数
# 如果一个模块经常变化就可以使用__import__()来动态载入
# __import__(name[, globals[, locals[, fromlist[, level]]]])  # name：模块名

complex()  # 用于创建一个值为real+imag * j的复数或者转化一个字符串或数为复数，如果第一个参数为字符串，则不需要指定第二个参数
# class complex([real[, imag]])  # real：int,long,float或字符串  imag：int,long,float  # complex(1)

hasattr()  # 用于判断对象是否包含对应的属性
# hasattr(object, name)  # object：对象  name：字符串，属性名
class Coordinate:
    x = 10
    y = 0
print1 = Coordinate()
print(hasattr(print1, 'x'))

round()  # 返回浮点数x的四舍五入值
# round(x[, n])  # x：数字表达式  n：表示从小数点位数，其中x需要四舍五入，默认值为0  # round(56.23, 1)

delattr()  # 用于删除属性
# delattr(x, 'foobar')相当于del x.foobar
# delattr(object, name)  # object：对象  name：必须是对象的属性
class Coordubate:
    x = 10
    y = 0
delattr(Coordinate, 'x')  # 删掉x属性

hash()  # 用于获取一个对象（字符串或数值等）的哈希值
# hash(object)  # object：对象  # hash('test')

memoryview()  # 返回给定参数的内存查看对象（Momory view）
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许python代码访问
# memoryview(obj)  # obj：对象  # v = memoryview('sun')   v[1]  # 'u'

set()  # 创建一个无序不重复元素集，可以进行关系测试，删除重复数据，还可以计算交集、差集、并集等
# class set([iterable])  # iterable：可迭代对象  # x = set('runoob')



