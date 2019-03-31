"""列表"""
# 序列是python中最基本的数据结构，序列中的每个元素都分配一个数字-它的位置，或索引，第一个索引是0，第二个索引是1，以此类推
# python有6个序列的内置类型，但最常见的是列表和元组
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员
# 此外，python已经内置确定序列的长度以及确定最大和最小的元素的方法
# 列表是最常见的python数据类型，它可以作为一个方括号内的逗号分隔值出现
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可，如下所示：
list1 = ['baidu', 'google', 'firox']
# 与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等

'''访问列表中的值'''
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
list2 = ['baidu', 'google', 11, 12]
print([1, 3])

'''更新列表'''
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：
list2 = ['baidu', 'google', 11, 12]
list2[2] = 111

'''删除列表元素'''
# 可以使用 del 语句来删除列表的的元素，如下实例：
list2 = ['baidu', 'google', 11, 12]
del list2[2]

'''python列表脚本操作符'''
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表，如下所示：
len([1, 2, 3])  # 结果：3   # 描述：长度
[1, 2, 3] + [4, 5, 6]  # 结果：[1, 2, 3, 4, 5, 6]  # 描述：组合
['is'] * 4   # 结果：['is', 'is', 'is', 'is']  # 描述：重复
3 in [1, 2, 3]  # 结果：True  # 描述：元素是否存在于列表中
for x in [1, 2, 3]:
    print(x, end='')  # 结果：1 2 3  # 描述：迭代

'''python列表截取与拼接'''
# python的列表截取与字符串操作类型，如下所示：
L = ['baidu', 'google', 'taobao']
L[2]  # 结果：'taobao'  # 读取第三个元素
L[-2]  # 结果：'google'  # 从右侧开始读取倒数第二个元素
L[1:]  # 结果：['google', 'taobao']  # 输出从第二个元素开始后的所有元素
# 列表还支持拼接操作：
squares = [1, 2, 3]
squares += [4, 5, 6]
print(squares)  # 结果为：[1, 2, 3, 4, 5, 6]

'''嵌套列表'''
# 使用嵌套列表即在列表里创建其它列表，例如：
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[0][1])  # 'b'

'''python列表函数和方法'''
# len()  # 返回列表元素个数
# len(list)  # list：要计算元素个数的列表  # list1=[1, 2, 3]  len(list1)

# max()  # 返回列表元素中的最大值
# max(list)  # list：要返回最大值的列表  # list1=[1, 2, 3]  max(list1)

# min()  # 返回列表元素中的最小值
# min(list)  # list：要返回最小值的列表  # list1=[1, 2, 3]  min(list1)

# list()  # 用于将元组或字符串转换为列表
# list( seq )  # seq：要转换为列表的元组或字符串  # str='baidu'  list(str)

# append()  # 用于在列表末尾添加新的对象
# list.append(obj)  # obj：添加到列表末尾的对象  # list1=['baidu', 'google']  list1.append('taobao')

# count()  # 用于统计某个元素在列表中出现的次数
# list.count(obj)  # obj：列表中统计的对象  # alist=[1, 'baidu', 1]  alist.count(1)

# extend()  # 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.extend(seq)  # seq：元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾
# language = ['baidu', 'google']  language_tuple = ('baidu', 'english')  language.extend(language_tuple)

# index()  # 用于从列表中找出某个值第一个匹配项的索引位置
# list.index(obj)  # obj：查找的对象  # list1=['baidu', 'google', 'taobao']  list1.index('taobao')

# insert() # 用于将指定对象插入列表的指定位置
# list.insert(index, obj)  # index：对象obj需要插入的索引位置  obj：要插入列表中的对象
# list1 = ['baidu', 'google', 'taobao']  list1.insert(1,'english')

# pop()  # 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.pop([index=-1])  # index：可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值
# list1 = ['baidu', 'google', 'taobao']  list1.pop(1)

# remove()  # 用于移除列表中某个值的第一个匹配项
# list.remove(obj)  # obj：列表中要移除的对象  # list1=['taobao', 'google', 'english']  list1.remove('taobao')

# reverse() # 用于反向列表中元素
# list.reverse()  # list1 = ['baidu', 'taobao', 'google']  list1.reverse()

# sort()  # 用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
# list.sort( key=None, reverse=False)  # key：主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
# 指定可迭代对象中的一个元素来进行排序。  reverse：排序规则，reverse = True 降序， reverse = False 升序（默认）
# vowels = ['e', 'a', 'u', 'o', 'i']  vowels.sort(reverse=True)

# clear()  # 用于清空列表，类似于 del a[:]
# list.clear()  # list1 = ['baidu', 'google', 'taobao']  list1.clear()

# copy()  # 用于复制列表，类似于 a[:]
# list.copy()  # list1=['baidu', 'taobao', 'google']  list2 = list1.copy()

