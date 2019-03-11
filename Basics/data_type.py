# 基本数据类型
dir()  # 对象   # 例子：dir(int)
help()  # 对象或对象＋方法   # 例子：help（int）  或者   help（int.imag）

# 需要背记的方法
int.bit_length()  # 作用是得到指定数值的二进制的长度数、宽度数
int.conjugate()
int.denominator  # 有理数在最低点的分母
int.from_bytes()  # res = int.from_bytes(x)的含义是把bytes类型的变量x，转化为十进制整数，并存入res中
int.imag()  # 复数的虚部
int.numerator()  # 有理数最低项的分子
int.real()  # 复数的实部
int.to_bytes()  # 功能：是int.from_bytes的逆过程，把十进制整数，转换为bytes类型的格式。

float.as_integer_ratio()
float.conjugate()
float.fromhex()
float.hex()
float.imag()  # 复数的虚部
float.is_integer()
float.real()  # # 复数的实部

bool.bit_length()
bool.conjugate()
bool.denominator()
bool.from_bytes()
bool.imag()
bool.numerator()
bool.real()
bool.to_bytes()

complex.conjugate()
complex.imag()
complex.real()

str.capitalize()
str.casefold()
str.center()
str.count()
str.encode()
str.endswith()
str.expandtabs()
str.find()
str.format()
str.format_map()
str.index()
str.isalnum()
str.isalpha()
str.isdecimal()
str.isdigit()
str.isidentifier()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()
str.join()
str.ljust()
str.lower()
str.lstrip()
str.maketrans()
str.partition()
str.replace()
str.rfind()
str.rindex()
str.rjust()
str.rpartition()
str.rsplit()
str.rstrip()
str.split()
str.splitlines()
str.startswith()
str.strip()
str.swapcase()
str.title()
str.translate()
str.upper()
str.zfill()

list.append()
list.copy()
list.count()
list.extend()
list.index()
list.insert()
list.pop()
list.remove()
list.reverse()
list.sort()

tuple.count()
tuple.index()

set.add()
set.clear()
set.copy()
set.difference()
set.difference_update()
set.discard()
set.intersection()
set.intersection_update()
set.isdisjoint()
set.issubset()
set.issuperset()
set.pop()
set.remove()
set.symmetric_difference()
set.symmetric_difference_update()
set.union()
set.update()

dict.clear()
dict.copy()
dict.fromkeys()
dict.get()
dict.items()
dict.keys()
dict.pop()
dict.popitem()
dict.setdefault()
dict.update()
dict.values()


# Python3 中有六个标准的数据类型：
# Number（数字）         int float bool complex
# String(字符串)         str
# List(列表)             list
# Tuple（元组）          tuple
# Set(集合)              set
# Dictionary(字典)       dict
# Python3的六个标准数据类型中：
# 不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）

"""Number（数字）"""
# python3支持int、float、bool、complex（复数）
# 可以用isinstance和type来判断类型
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
# 5 + 4 # 加法
# 4.3 - 2 # 减法
# 3 * 7 # 乘法
# 2 / 4 # 除法，得到一个浮点数
# 2 // 4 # 除法，得到一个整数
# 17 % 3 # 取余
# 2 ** 5 # 乘方

# python可以同时为多个变量赋值，如：a, b = 1, 2
# 一个变量可以通过赋值指向不同类型的对象
# 数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数
# 在混合计算时，python会把整型转换为浮点数
# python还支持复数，复数由实数部分和虚数部分构成，可以用a+bj，或者complex(a,b)表示，复数的实数a和虚部b都是浮点数

"""String（字符串）"""
# python中的字符串用单引号''或双引号""括起来，同时使用反斜杠\转义特殊字符
# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以0为开始值，-1为从末尾的开始位置
# 从后面索引：  -6  -5  -4  -3  -2  -1
# 从前面索引：  0    1   2   3   4   5
#               a    b   c   d   e   f
# 从前面截取：  :    1   2   3   4   5
# 从后面截取：  :   -5  -4  -3  -2  -1
# 加号+是字符串的连接符；星号*表示复制当前字符串，紧跟的数字为复制的次数；
# python使用反斜杠（\）转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串的前面添加r，表示原始字符串
# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

"""List（列表）"""
# List（列表）是python中使用最频繁的数据类型
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号[]之间，用逗号分隔开的元素列表
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
#         t = ['a', 'b', 'c', 'd', 'e']
# 从前面索引：  0    1    2    3    4
# 从后面索引： -5   -4   -3   -2   -1
# t = [1:3]     返回  ['b', 'c']
# t = [3:]      返回  ['d', 'e']
# t = [:4]      返回  ['a', 'b', 'c', 'd']
# t = [:]       返回  ['a', 'b', 'c', 'd', 'e']

# 加号+是列表连接运算符，星号*是重复操作，如下实例：
list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list1)  # 输出完整列表
print(list1[0])  # 输出列表第一个元素
print(list1[1:3])  # 从第二个开始输出到第三个元素
print(list1[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list1 + tinylist)  # 连接列表
# 与python字符串不一样的是，列表中的元素是可以改变的

# python列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引1到索引4的位置并设置为步长为2（间隔一个位置）来截取字符串：
#   索引      0    1    2    3    4    5    6
# letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
# letters[1:4:2]     返回  ['h', 'c']

"""Tuple（元组）"""
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tinytuple * 2)     # 输出两次元组
print(tuple + tinytuple)  # 连接元组
# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置，也可以进行截取。
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构建包含0个或者1个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
# string（字符串）、list（列表）和tuple（元组）都属于sequence（序列）

"""Set（集合）"""
# Set（集合）是由一个或数个形态各异的大小整体组成的，构建集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
# parame = {value01, value02, ...}    或者       set(value)
# 实例：
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

"""Dictionary（字典）"""
# Dictionary（字典）是python中另一个非常有用的内置数据类型
# 列表是有序的对象集合，字典是无序的对象集合，两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过便宜存取。
# 字典是一种映射类型，字典用{}标识，它是一个无序的键(key):值(value)的集合。
# 键（key）必须使用不可变类型。
# 在同一个字典中，键（key）必须是唯一的。
dict = {}  # 创建空字典
dict['one'] = '菜鸟教程'
dict[2] = '菜鸟工具'
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.baidu.com'}
print(dict['one'])  # 输出键为'one'的值
print(dict[2])  # 输出键为2的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

"""Python数据类型转换"""
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
x =1
int(x[, base])  # 将x转换为一个整数
float(x)  # 将x转换到一个浮点数
complex(real[,imag])  # 创建一个复数
str(x)  # 将对象x转换为字符串
repr(x)  # 将对象x转换为表达式字符串
eval(str)  # 用来计算在字符串中的有效python表达式，并返回一个对象
tuple(x)  # 将序列x转换为一个元组
list(x)  # 将序列x转换为一个列表
set(x)  # 将序列x转换为可变集合
dict(d)  # 创建一个字典，d必须是一个序列（key,value)元组
frozenset(s)  # 转换为不可变集合
chr(x)  # 将一个整数转换为一个字符
ord(x)  # 将一个字符转换为它的整数值
hex(x)  # 将一个整数转换为一个十六进制字符串
oct(x)  # 将一个整数转换为一个八进制字符串

