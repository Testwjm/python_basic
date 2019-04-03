"""OS文件/目录方法"""
# os模块提供了非常丰富的方法用来处理文件和目录，常用的方法如下表所示：

# os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试
# os.access(path, mode)  # path：要用来检测是否有访问权限的路径
# mode：mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行
# import os
# x = os.access('D:\easy_log.xlsx', os.F_OK)
# print(x)

# os.chdir() 方法用于改变当前工作目录到指定的路径
# os.chdir(path)  # path：要切换到的新路径
# import os
# z = os.getcwd()  # 查看当前工作目录
# print(z)
# path = '\www'
# y = os.chdir(path)  # 修改当前工作目录
# print(y)

# os.chflags() 方法用于设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来
# 只支持在 Unix 下使用
# os.chflags(path, flags)  # path：文件名路径或目录路径
# flags -- 可以是以下值：
# stat.UF_NODUMP: 非转储文件
# stat.UF_IMMUTABLE: 文件是只读的
# stat.UF_APPEND: 文件只能追加内容
# stat.UF_NOUNLINK: 文件不可删除
# stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED: 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
# stat.SF_APPEND: 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT: 快照文件(超级用户可设)
# import os
# import stat
# path = 'D:\easy_log.xlsx'
# flags = stat.SF_NOUNLINK  # 为文件设置标记，使得它不能被重命名和删除
# s = os.chflags(path, flags)  # 只支持在 Unix 下使用
# print(s)

# os.chmod() 方法用于更改文件或目录的权限
# Unix 系统可用
# os.chmod(path, mode)  # path：文件名路径或目录路径
# flags：可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表，执行权限表示可以把工作目录切换到此目录 ，
# 删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
