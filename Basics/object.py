"""面向对象"""
# 类（class）：用来描述具有相同的属性和方法的对象的集合，它定义了该集合中每个对象所共有的属性和方法，对象是类的实例
# 方法：类中定义的函数
# 类变量：类变量在整个实例化的对象中是公立的，类变量定义在类中且在函数体之外，类变量通常不作为实例变量使用
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关数据
# 方法重写：如果父类继承下来的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写
# 局部变量：定义在方法中的变量，只作用于当前实例的类
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法，继承也允许把一个派生类的对象作为一个基类的对象对待，
# 例如，有这样一个设计，一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）
# 实例化：创建一个类的实例，类的具体对象
# 对象：通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法
# python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法
# 对象可以包含任意数量和类型的数据

# 类定义
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# 类对象
# 类对象支持两种操作：属性引用和实例化
# 属性引用使用和python中的所有的属性引用一样的标准语法：obj.name
# 类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
class Myclass:
    """一个简单的实例"""
    i = 12345
    def f(self):
        return "hello world"

# 实例化类
x = Myclass
# 访问类的属性和方法
print('Myclass类的属性i为：', x.i)
print('Myclass类的方法f输出为：', x.f())

# 类有一个名为__init__()的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
def __init__(self):
    self.data = []

# 当然__init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上，例如：
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# self代表类的实例，而非类
# 类的方法和普通的函数只有一个特别的区别，它们必须有一个额外的第一个参数名称，按照惯例它的名称是self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

t = Test()
t.prt()

# 类的方法
# 在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类的方法必须包含参数self，且为第一参数，self代表的是类的实例
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁"%(self.name, self.age))

p = people('wjm', 10, 20)
p.speak()

# 继承
# 派生类的定义如下所示:
# class DerivedClassName(BaseClassName1):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
# 从左到右查找基类中是否包含方法。
# BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
# class DerivedClassName(modname.BaseClassName):
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s说：我%d岁了"%(self.name, self.age))

# 单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s说：我%d岁了，读%d年级"%(self.name, self.age, self.grade))

s = student('wjm', 10, 60, 3)
s.speak()

# 多继承
# 多继承的类定义形如下例:
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
# 从左到右查找父类中是否包含方法。
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s说：我%d岁了' % (self.name, self.age))

# 单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s说：我%d岁了，读%d年级"%(self.name, self.age, self.grade))

# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s，我是演讲家，我演讲的主题是%s"%(self.name, self.topic))

# 多重继承
class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample('wjm', 10, 60, 3, '三毛')
test.speak()  #方法名同，默认调用的是在括号中排前地父类的方法

# 方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类的方法')

class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
# super() 函数是用于调用父类(超类)的一个方法。

# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
# 类的私有属性实例如下：
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)  # 报错，实例不能访问私有变量

# 类的私有方法实例如下：
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 运算符重载
# Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)'%(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)










