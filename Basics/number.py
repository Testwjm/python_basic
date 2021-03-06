"""数字(number)"""
# python数字数据类型用于存储数值
# 数据类型是不允许改变的，这就意味着如果改变数字数据类型的值，将重新分配内存空间
# python支持三种不同的数值类型：
# 整型（int）：通常被称为是整型或整数，是正或负整数，不带小数点，python3整型是没有限制大小的，可以当做Long类型使用，所以python3没有python2的Long类型
# 浮点型（float）：浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数表示（2.5e2 = 2.5 x 102 = 250）
# 复数（complex）：复数由实数部分和虚数部分构成，可以用a+bj或者complex(a,b)表示，复数的实部a和虚部b都是浮点数

# python数字类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

# 数学函数
# abs(x)  描述：返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)  描述：返回一个大于或等于 x 的的最小整数，如math.ceil(4.1) 返回 5、math.ceil(-45.17)返回-45
# floor(x)  描述：返回数字的下舍整数，小于或等于 x，如math.floor(4.9)返回 4
# exp(x)  描述：返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)  描述：返回数字的绝对值，如math.fabs(-10) 返回10.0
# log(x)  描述：log() 方法返回x的自然对数，x > 0，如math.log(1)
# log10(x)	描述：log10() 方法返回以10为基数的x对数，x>0，如math.log10(1)
# max(x1, x2,...)  描述：返回给定参数的最大值，参数可以为序列，如max(1, 11, 111)
# min(x1, x2,...)  描述：返回给定参数的最小值，参数可以为序列，如min(-1, -11, -111)
# modf(x)  描述：返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，如math.modf(1.12)
# pow(x, y)  描述：x**y 运算后的值，如pow(10, 2)
# round(x [,n])  描述：返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数，如round(1.234, 2)
# sqrt(x)  描述：返回数字x的平方根，如math.sqrt(9)

# 随机数函数
# choice(seq)  # 返回一个列表，元组或字符串的随机项
# import random   random.choice(seq)  # seq：可以是一个列表，元组或字符串
# random.choice(range(10))  random.choice([1, 2, 3])   random.choice('ran')

# randrange()  # 返回指定递增基数集合中的一个随机数，基数缺省值为1
# import random  random.randrange([start,] stop[, step])  # start：指定范围内的开始值，包含在范围内  stop：指定范围内的结束值，
# 不包含在范围内  step：指定递增基数
# random.randrange(1,6,2)  random.randrange(100)

# random()  # 返回随机生成的一个实数，它在0到1范围内
# import random  random.random()  # 没有参数  # random.random()

# seed()  # 改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数
# import random  random.seed([x])  # 改变随机数生成器的种子seed，如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed
# import random  random.seed()  print ("使用默认种子生成随机数：", random.random())
# random.seed(10)  print ("使用整数种子生成随机数：", random.random())
# random.seed('hello', 2)  print ("使用字符串种子生成随机数：", random.random())

# shuffle()  # 将序列的所有元素随机排序
# import random  random.shuffle(lst)  # lst：列表
# list = [1, 2, 5, 10]  random.shuffle(list)

# uniform()  # 将随机生成下一个实数，他在[x,y]范围内
# import random  random.uniform(x, y)  # x：随机数的最小值  y：随机数的最大值  # random.unform(1, 5)

# 三角函数
# acos()  # 返回x的反余弦弧度值
# import math  math.acos(x)  # x：-1到1之间的数值，如果x是大于1，会产生一个错误值  # math.acos(0.64)

# asin()  # 返回x的反正弦弧度值
# import math math.asin(x)  # x：-1到1之间的数值，如果x是大于1.会产生一个错误值  # math.asin(0.64)

# atan()  # 返回x的反正切弧度值
# import math math.atan(x)  # x：一个数值  # math.atan(10)

# atan2()  # 返回给的的x及y坐标值的反正切值
# import math  math.atan2(y, x)  # x,y：一个数值  #  math.atan2(10, 20)

# cos()  # 返回x的弧度的余弦值
# import math  math.cos(x)  # x：一个数值  # math.cos(3)

# hypost()  # 返回欧几里德范数 sqrt(x*x + y*y)
# import math  math.hypost(x,y)  # x,y：一个数值  # math.hypost(3, 2)

# sin()  # 返回x的弧度的正弦值
# import math  math.sin(x)  # x：一个数值  # math.sin(3)

# tan()  # 返回x的弧度的正切值
# import math math.tan(x)  # x：一个数值  # math.tan(3)

# degrees()  # 将弧度转换为角度
# import math math.degrees(x)  # x：一个数值  # math.degrees(3)

# radians()  # 将角度转换为弧度
# import math  math.radians(x)  # x：一个数值  # math.radians(3)

# 数学常量
# 常量：pi  # 描述：数学常量pi（圆周率，一般以π来表示）
# 常量：e   # 描述：数学常量e，e即自然常数（自然常数）
