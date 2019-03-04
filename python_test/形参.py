def fun1(a, b, c):
    print(a, b, c)


def fun2(a, *args):  #args为元组
    print(a)
    print(sum(args))


def fun3(a, **kwargs):  #args为元组
    print(a)
    print(kwargs["b"])


a = [1, 2, 3]
fun1(*a)
fun2(1, 2, 3)
b = {'b': 5, 'c': 7}
fun1(1, **b)  #传入字典
fun3(1, b=3, d=5)  #不能传入字典
