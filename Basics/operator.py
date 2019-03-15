# 运算符
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

