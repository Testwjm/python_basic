"""函数"""


# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段
# 函数能提高应用的模块性，和代码的重复利用率，你已经知道python提供了许多内建函数，比如print()，但你也可以自己创建函数，这被叫做用户自定义函数
# 你可以定义一个由自己想要功能的函数，以下是简单的规则:
# 函数代码块以def关键词开头，后接函数标识符名称和圆括号（）
# 任何传入参数的自变量必须放在圆括号中间，圆括号之间可以用于定义参数
# 函数的第一行语句可以选择性的使用文档字符串，用于存放函数说明
# 函数内容以冒号起始，并且缩进
# return[表达式]结束函数，选择性的返回一个值给调用方，不带表达式的return相当于返回None
# python定义函数使用def关键字，一般格式如下：
# def 函数名（参数列表）：
#     函数体
def area(width, height):
    return width * height


def print_welcome(name):
    print("welcome", name)


if __name__ == "__main__":
    print_welcome("run")
    w = 4
    h = 5
    print("width=", w, "height", h, "area=", area(w, h))

# 函数调用
#
