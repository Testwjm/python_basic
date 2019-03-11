# 基础语法

# 标识符(变量名)
# 第一个字符必须是字母表中字母或下划线_.
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感。

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
input('\n\n按下 enter 键后退出')  # "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
# 不换行输出
print(x, end='')
print(y, end='')

# 在python用import或者from...import来导入相应的模块
# 将整个模块（somemodule)都导入，格式为：import somemodule
# 从某个模块中导入某个函数，格式为：from somemodule import somefunction
# 从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为：from somemodule import *
"""导入sys模块"""
import sys
print('             python import mode          ')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
"""导入sys模块的argv，path成员"""
from sys import argv,path  # 导入特定的成员
print('        python from import       ')
print('path:', path)  # 因为已经导入path成员，所以此次引用时不需要加sys.paths

