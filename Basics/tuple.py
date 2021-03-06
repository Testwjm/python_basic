"""元组"""
# python的元组与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号，列表使用方括号
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
tup1 = ('baidu', 'google', 1, 11)
tup2 = 'a', 'b', 1, '11'  # 不用括号也可以
tup3 = ()  # 创建空元组

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup4 = (50,)  # 加上逗号，类型为元组
type(tup4)

'''访问元组'''
# 元组可以使用下标索引来访问元组中的值，如下实例:
tup1 = ('baidu', 'google', 1, 11)
print(tup1[0])

'''修改元组'''
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup1 = ('a', 'b', 'c')
tup2 = (1, 2, 3)
tup3 = tup1 + tup2

'''删除元组'''
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup1 = ('baidu', 'google', 1, 11)
del tup1

'''元组运算符'''
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
len((1, 2, 3))  # 结果：3  描述：计算元素个数
(1, 2, 3) + (4, 5, 6)  # 结果：(1, 2, 3, 4, 5, 6)  # 描述：连接
('is', * 4)  # 结果：('is', 'is', 'is', 'is')  # 描述：复制
3 in (1, 2, 3)  # 结果：True  # 描述：元素是否存在
for x in (1, 2, 3):
    print(x,)  # 结果：1 2 3  # 迭代

'''元组索引，截取'''
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
L = ('baidu', 'google', 'taobao')
L[2]  # 结果：'toabao'  # 描述：读取第三个元素
L[-2]  # 结果：'google'  # 描述：反向读取，读取倒数第二个元素
L[1:]  # 结果：('google', 'taobao')  # 描述：截取元素，从第二个开始后的所有元素

'''元组内置函数'''
# len(tuple)  # 计算元组元素个数
# tuple1 = ('baidu', 'google', 'taobao')  len(tuple1)

# max(tuple)  # 返回元组中元素最大值
# tuple1 = ('1', '2', '3')  max(tuple1)

# min(tuple)  # 返回元组中元素最小值
# tuple1 = ('1', '2', '3')  max(tuple1)

# tuple(seq)  # 将列表转换为元组
# list1 = ['1', '2', '3']  tuple(list1)
