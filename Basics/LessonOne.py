"""基础语法"""
'''编码'''
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
# -*- coding: cp-1252 -*-
# 上述定义允许在源文件中使用 Windows-1252 字符集中的字符编码，对应适合语言为保加利亚语、白罗斯语、马其顿语、俄语、塞尔维亚语

'''标识符(变量名)'''
# 第一个字符必须是字母表中字母或下划线_.
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感。

'''保留字（关键字）'''
# 保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
import keyword

keyword.kwlist

'''注释'''
# Python中单行注释以 # 开头，实例如下：
# 第一个注释
# 多行注释可以用多个 # 号，还有 ''' 和 """：
# 第一个注释
# 第二个注释
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""

'''行与缩进'''
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print('True')
else:
    print('False')

'''多行语句'''
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
total = item_one + \
        item_two + \
        item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
tota2 = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

'''数字（Number）类型'''
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True、False。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j

'''字符串（String）'''
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

string = 'Runoob'
print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始的后的所有字符
print(string * 2)  # 输出字符串两次
print(string + '你好')  # 连接字符串
print('hello\nrunoob')  # 使用反斜杠（\）+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个r，表示原始字符串，不会发生转义

'''空行'''
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
# 但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分

'''等待用户输入'''
input('\n\n按下 enter 键后退出')  # "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

'''同一行显示多条语句'''
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

'''多个语句构成代码组'''
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
# 如下实例：
if expression:
    suite
elif expression:
    suite
else:
    suite

'''Print 输出'''
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
# 不换行输出
print(x, end='')
print(y, end='')

'''import 与 from...import'''
# 在python用import或者from...import来导入相应的模块
# 将整个模块（somemodule)都导入，格式为：import somemodule
# 从某个模块中导入某个函数，格式为：from somemodule import somefunction
# 从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为：from somemodule import *
# 导入sys模块
import sys
print('             python import mode          ')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
# 导入sys模块的argv，path成员
from sys import argv, path  # 导入特定的成员
print('        python from import       ')
print('path:', path)  # 因为已经导入path成员，所以此次引用时不需要加sys.paths
