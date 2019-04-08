""" 编程第一步---条件控制---循环语句"""
'''end关键字'''
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
a, b = 0, 1
while b < 10:
    print(b, end='')
    a, b = b, a + b

'''if语句'''
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else
age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("你是在逗我吧！")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄：", human)
# 退出提示
input("点击enter键退出")

number = 7
guess = -1
print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了。。。")
    elif guess > number:
        print("菜的数字大了。。。")

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，但不能整除3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")

# while 循环
# python中while语句的一般形式：
# while 判断条件：
#        语句
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到%d之和为：%d" % (n, sum))

# 无限循环
# 我们可以通过设置条件表达式永远不为false来实现无限循环，实例如下：
var = 1
while var == 1:  # 表达式永远为true
    num = int(input("请输入一个数字："))
    print("你输入的数字是：", num)
print("Good bye!")

# while循环使用else语句
# 在while...else在条件语句为false时执行else的语句块：
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")

# 简单语句组
# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中，如下所示：
flag = 1
while (flag): print('欢迎访问')
print("Good Bye")

# for循环
# python中for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# for循环的一般格式如下：
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

# 以下for实例中使用了break语句，break语句用于跳出当前循环：
sites = ["baidu", "Google", "Tunn", "taobao"]
for site in sites:
    if site == "Google":
        print("谷歌")
        break
    print("循环数据" + site)
else:
    print("没有循环数据")
print("完成循环")

# range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数，它会生成数列，例如：
for i in range(5):
    print(i)
# 你还可以结合range()和len（）函数以遍历一个序列的索引，如下所示：
a = ['Google', 'baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# break和continue语句及循环中的else子句
# break语句可以跳出for和while的循环体，如果你从for或while循环中终止，任何对应的循环else块将不执行，实例如下：
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为：', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值为：', var)
    var = var - 1
    if var == 5:
        break
print('Good Bye')

# countinue语句被用来告诉python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':
        continue
    print('当前字母:', letter)

var = 10
while var > 0:  # 第二个实例
    var = var -1
    if var == 5:
        continue
    print('当前变量值：', var)
print("Good Bye")

# 循环语句可以有else子句，它在穷尽列表（以for循环）或条件变为false（以while循环）导致循环终止时被执行，但循环被break终止时不执行
# 如下实例用于查询质数的循环例子：
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:  # 循环中没有找到元素
        print(n, '是质数')

# pass语句
# pyhon中pass是空语句，是为了保持程序结构的完整性
# pass不做任何事情，一般用做占位语句，如下实例
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行pass块')
    print('当前字母:', letter)
print('Good bye!')

