"""字典"""
# 字典是另一种可变容器模型，且可存储任意类型对象
# 字典的每个键值（key=>value）对用冒号（：）分割，每个对之间用逗号（，）分割，整个字典包括在花括号（{}）中，格式如下所示：
# d = {key1 : value1,key2 : value2}
# 键必须是唯一的，但值则不必
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
# 一个简单的字典实例：
dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

'''访问字典里的值'''
# 把相应的键放入到方括号中，如下实例:
dict2 = {'name': 'run', 'age': '18', 'class': 'one'}
print(dict2['name'])

'''修改字典'''
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict3 = {'name': 'run', 'age': '18', 'class': 'one'}
dict3['age'] = 22  # 更新age
dict3['school'] = '学校'  # 添加信息

'''删除字典元素'''
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令，如下实例：
dict4 = {'name': 'run', 'age': '18', 'class': 'one'}
del dict4['name']  # 删除键值'name'
dict4.clear()  # 清空字典
del dict4  # 删除字典

'''字典键的特性'''
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1、不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict5 = {'name': 'run', 'age': '18', 'name': '小鸟'}
print(dict5['name'])
# 2、键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
dict6 = {['Name']: 'Runoob', 'Age': 7}
print(dict6['Name'])

'''字典内置函数和方法'''
# len(dict)  # 计算字典元素个数，即键的总数
# dict = {'name': 'run', 'age': '18', 'class': 'one'}    len(dict)

# str(dict)  # 输出字典，以可打印的字符串表示
# dict = {'name': 'run', 'age': '18', 'class': 'one'}    str(dict)

# type(variable)  # 返回输入的变量类型，如果变量是字典就返回字典类型
# dict = {'name': 'run', 'age': '18', 'class': 'one'}    type(dict)

# clear()  # 用于清空字典内所有元素
# dict.clear()  # dict = {'name': 'run', 'age': '18', 'class': 'one'}   dict.clear()

# copy()  # 返回一个字典的浅复制
# dict.copy()  # dict = {'name': 'run', 'age': '18', 'class': 'one'}  dict2 = dict.copy()

# fromkeys()  # 用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
# dict.fromkeys(seq[, value])  # seq：字典键值列表  value：可选参数, 设置键序列（seq）对应的值，默认为 None
# seq = ('name', 'age', 'class')  dict.fromkeys(seq, 10)

# get()  # 返回指定键的值，如果值不在字典中返回默认值
# dict.get(key, default=None)  # key：字典中要查找的键   default：如果指定键的值不存在时，返回该默认值None
# # dict = {'name': 'run', 'age': '18', 'class': 'one'}  dict.get('age')

# in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
# 而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true
# key in dict  # key：要在字典中查找的键
dict1 = {'name': 'run', 'age': '22', 'class': 'one'}
if 'age' in dict1:
    print('age,存在')
else:
    print('age,不存在')

# items() # 以列表返回可遍历的(键, 值) 元组数组
# dict.items()  # dict1 = {'name': 'run', 'age': '22', 'class': 'one'}  dict1.items()

#  keys()  # 返回一个可迭代对象，可以使用 list() 来转换为列表
# dict.keys()  # dict1 = {'name': 'run', 'age': '22', 'class': 'one'}  dict1.keys()  list(dict1.keys())

#  setdefault() 方法和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
# dict.setdefault(key, default=None)  # key：查找的键值   default：键不存在时，设置的默认键值
# dict1 = {'name': 'run', 'age': '12', 'class': 'one'}  dict1.setdefault('name')

# update()  # 把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
# dict.update(dict2)  # dict2：添加到指定字典dict里的字典
# dict1 = {'name': 'run', 'age': '18'}  dict2 = {'class': 'one'}  dict1.update(dict2)

# values()  # 返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值
# dict.values()  # dict1 = {'name': 'run', 'age': '18', 'class': 'one'}  list(dict1.values())

#  pop()  # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
# pop(key[,default])  # key: 要删除的键值  default: 如果没有 key，返回 default 值
# dict1 = {'name': 'run', 'age': '22', 'calss': 'one'}  dict1.pop('name')

# popitem()  # 随机返回并删除字典中的一对键和值(一般删除末尾对)
# 如果字典已经为空，却调用了此方法，就报出KeyError异常
# popitem()  # dict1 = {'name': 'run', 'age': '22', 'class': 'one'}  dict1.popitem()

