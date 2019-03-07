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

