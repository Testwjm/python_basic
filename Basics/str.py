"""字符串"""
# 字符串是python中最常用的数据类型，我们可以使用引号（'或"）来创建字符串
# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
var1 = 'Hello World!'
var2 = 'Runoob'
print(var1[0])
print(var2[1:5])

'''python转义字符'''
# 在需要在字符中使用特殊字符时，python用反斜杠（\）转义字符
# \（在行尾时）  描述：续行符     \\  描述：反斜杠符号
# \'  描述：单引号                \"  描述：双引号
# \a  描述：响铃                  \b  描述：退格（Backspace）
# \e  描述：转义                  \000  描述：空
# \n  描述：换行                  \v  描述：纵向制表符
# \t  描述：横向制表符            \r  描述：回车
# \f  描述：换页                  \oyy  描述：八进制数，yy代表的字符，例如：\o12代表换行
# \xyy  描述：十六进制数，yy代表的字符，例如：\x0a代表换行
# \other  描述：其它的字符以普通格式输出

'''python字符串运算符'''
# 例子，变量a值为字符串‘hello’，变量b值为字符串‘python’
# +  描述：字符串连接  # a+b输出结果：hellopython
# *  描述：重复输出字符串  # a*2输出结果：hellohello
# []  描述：通过索引获取字符串中的字符  # a[0]输出结果：h
# [:]  描述：截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的  # a[0:2]输出结果：he
# in  描述：成员运算符 - 如果字符串中包含给定的字符返回 True  # 'h' in a输出结果：True
# not in 描述：	成员运算符 - 如果字符串中不包含给定的字符返回 True  # 'x' not in a输出结果
# r/R  描述：原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符，
#  原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# print(r'\n')  # print(R'\n')

'''python字符串格式化'''
# Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
# 在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))  输出结果：我叫 小明 今年 10 岁!

# python字符串格式化符号:
# %c  描述：格式化字符及其ASCII码
# %s  描述：格式化字符串
# %d  描述：格式化整数
# %u  描述：格式化无符号整型
# %o  描述：格式化无符号八进制数
# %x  描述：格式化无符号十六进制数
# %X  描述：格式化无符号十六进制数（大写）
# %f  描述：格式化浮点数字，可指定小数点后的精度
# %e  描述：用科学计数法格式化浮点数
# %E  描述：作用同%e，用科学计数法格式化浮点数
# %g  描述：%f和%e的简写
# %G  描述：%f和%E的简写
# %p  描述：用十六进制数格式化变量的地址

# 格式化操作符辅助指令:
# *  描述：定义宽度或者小数点精度
# -  描述：用做左对齐
# +  描述：在正数前面显示加号（+）
# <sp>  描述：在正数前面显示空格
# #  描述：在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0  描述：显示的数字前面填充‘0’而不是默认的空格
# %  描述：'%%'输出一个单一的'%'
# (var)  描述：映射变量（字典参数）
# m.n.  描述：m是显示的最小总宽度，n是小数点后的位数（如果可用的话）

'''python三引号'''
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下：
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

'''Unicode字符串'''
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。

'''python的字符串内建函数'''
# capitalize()  # 将字符串的第一个字母变成大写，其他字母变小写
# str.capitalize()  #  a = 'CAT'  a.capitalize()  返回：Cat

# center()  # 返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格
# str.center(width[, fillchar])  # width：字符串的总宽度  # fillchar：填充字符  a = 'www.baidu.com'  a.center(40, '*')

# count()  # 用于统计字符串里某个字符出现的次数，可选参数为在字符串搜索的开始与结束位置。
# str.count(sub, start= 0,end=len(string))  # sub：搜索子字符串  start：字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0
# end：字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置
# a = 'www.baidu.com'  sub='w'  a.count(sub, 0, 10)

# decode()  # 以指定的编码格式解码bytes对象，默认编码为‘utf-8’
# bytes.decode(encoding='utf-8', errors='strict')  # encoding：要使用的编码，如‘utf-8’  errors：设置不同错误的处理方案，
# 默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
# 以及通过 codecs.register_error() 注册的任何值
# a='百度'  a.encode('UTF-8', 'strict').decode('utf-8','strict')

# encode()  # 以指定的编码格式编码字符串，errors参数可以指定不同的错误处理方案
# str.encode(encoding='UTF-8', errors='strict')  # encoding：要使用的编码，如：UTF-8   errors：设置不同错误的处理方案，
# 默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
# 以及通过 codecs.register_error() 注册的任何值。
# a = '百度'  a.encode('UTF-8', 'strict')

# endswith()  # 用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置
# str.endswith(suffix[, start[, end]])   # suffix：该参数可以是一个字符串或者是一个元素   start：字符串中的开始位置  end：字符中结束位置
# str = 'run'  s = 'n'  str.endswith(s)

# expandtabs()  # 把字符串中的tab符号('\t')转为空格，tab符号('\t')默认的空格是8
# str.expandtabs(tabsize=8)   # tabsize：指定转换字符串中的 tab 符号('\t')转为空格的字符数
# a  = 'this is\tstring'   a.expandtabs(16)

# find()  # 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1
# str.find(str, beg=0, end=len(string))  # str：指定检索的字符串  beg：开始索引，默认为0  end：结束索引，默认为字符串的长度
# str1 = "Runoob example....wow!!!"  str2 = "exam"  str1.index(str2)

# index()  # 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常
# str.index(str, beg=0, end=len(string))  # str：指定检索的字符串  # beg：开始索引，默认为0  # end：结束索引，默认为字符串的长度
# str1 = "Runoob example....wow!!!"  str2 = "exam"  str1.index(str2)

# isalnum()  # 检测字符串是否由字母和数字组成
# str.isalnum()  # str = "runoob2016"  str.isalnum()

