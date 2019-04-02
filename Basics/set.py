"""集合"""
# 集合（set）是一个无序的不重复元素序列
# 可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set（）而不是{}，因为{}是用来创建一个空字典，创建格式：
# parame = {value01,value02,...}   或者   set(value)

'''添加元素'''
# s.add(x)  # 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
# thisset = set(('name', 'age', 'class'))  thisset.add('new')

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update(x)
# thisset = set(('name', 'age', 'class'))  thisset.update([1, 2])

'''移除元素'''
# s.remove(x)  # 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
# thisset = set(('name', 'age', 'class'))  thisset.remove('name')

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# s.discard(x)
# thisset = set(('name', 'age', 'class'))  thisset.discard('age')

# 我们也可以设置随机删除集合中的一个元素，语法格式如下：
# s.pop()
# thisset = set(('name', 'age', 'class'))  thisset.pop()

'''计算集合元素个数'''
# len(s)
# thisset = set(('name', 'age', 'class'))  len(thisset)

'''清空集合'''
# s.clear()
# thisset = set(('name', 'age', 'class'))  thisset.clear()

'''判断元素是否在集合中存在'''
# x in s  # 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False
# thisset = set(('name', 'age', 'class'))  'name' in thisset

'''集合内置方法完整列表'''
# add()  # 用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
# set.add(elmnt)  # elmnt：必需，要添加的元素  # thisset = set(('name', 'age', 'class'))  thisset.add('new')

# clear()  # 用于移除集合中的所有元素
# set.clear()  # thisset = set(('name', 'age', 'class'))  thisset.clear()

# copy()  # 用于拷贝一个集合
# set.copy()  # thisset = set(('name', 'age', 'class'))  thisset2 = thisset.copy()

# difference()  # 用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
# set.difference(set)  # set：必需，用于计算差集的集合
# x = {'1', '2', '3'}  y = {'1', '4', '5'}  z = x.difference(y)  print(z)  # 结果：{'2', '3'}

# difference_update() # 用于移除两个集合中都存在的元素
# difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，
# 而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值
# set.difference_update(set)  # set：必需，用于计算差集的集合
# x = {'1', '2', '3'}  y = {'1', '4', '5'}  z = x.difference_update(y)  print(z)  # 结果：{'2', '3'}

# discard() 方法用于移除指定的集合元素
# 该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会
# set.discard(value)  # value：必需，要移除的元素  thisset = set(('name', 'age', 'class'))  thisset.discard('name')

# intersection()  # 用于返回两个或更多集合中都包含的元素，即交集
# set.intersection(set1, set2 ... etc)  # set1：必需，要查找相同元素的集合  set2：可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
# x = {'1', '2', '3'}  y = {'1', '4', '5'}  z = x.intersection(y)  print(z)  # 结果：{'1'}

# intersection_update() # 用于获取两个或更多集合中都重叠的元素，即计算交集
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素
# set.intersection_update(set1, set2 ... etc)  # set1：必需，要查找相同元素的集合  set2：可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
# x = {'1', '2', '3'}  y = {'1', '4', '5'}  z = x.intersection_update(y)  print(z)  # 结果：{'1'}

# isdisjoint()  # 用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
# set.isdisjoint(set)  # set：必需，要比较的集合
# x = {'1', '2', '3'}  y = {'1', '4', '5'}  z = x.isdisjoint(y)  print(z)  # 结果：True

# issubset()  # 用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False
# set.issubset(set)  # set：必需，要比查找的集合
# x = {'1', '2', '3'}  y = {'1', '2', '4', '3', '5'}  z = x.issubset(y)  print(z)  # 结果：True

# issuperset()  # 用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
# set.issuperset(set)  # set： 必需，要比查找的集合
# x = {'1', '2', '3', '4', '5'}  y = {'1', '2', '3'}  z = x.issuperset(y)  print(z)  # 结果：True

# pop()  # 用于随机移除一个元素
# set.pop()  # thisset = set(('name', 'age', 'class'))  thisset.pop()

# remove()  # 用于移除集合中的指定元素
# 该方法不同于 discard() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会
# set.remove(item)  # item：要移除的元素  # thisset = set(('name', 'age', 'class'))  thisset.remove('age')

# symmetric_difference()  # 返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素
# set.symmetric_difference(set)  # set：集合
# x = {'1', '2', '3'}  y = ('3', '4', '5')  z = x.symmetric_difference(y)  print(z)  # 结果：{'1', '2', '4', '5'}

# symmetric_difference_update()  # 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
# set.symmetric_difference_update(set)  # set：要检测的集合
# x = {'1', '2', '3'}  y = ('3', '4', '5')  z = x.symmetric_difference_update(y)  print(z)  # 结果：{'1', '2', '4', '5'}

# union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
# set.union(set1, set2...)  # set1：必需，合并的目标集合  set2：可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开
# x = {'1', '2', '3'}  y = ('3', '4', '5')  z = x.union(y)  print(z)  # 结果：{'1', '2', '3', '4', '5'}

# update()  # 用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略
# set.update(set)  # set：必需，可以是元素或集合
# x = {'1', '2', '3'}  y = ('3', '4', '5') x.update(y) # 结果：{'1', '2', '3', '4', '5'}
