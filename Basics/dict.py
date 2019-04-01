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
