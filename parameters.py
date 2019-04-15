# 定义函数时给定的名称为 形参(parameters)
# 调用函数时提供的函数值为 实参(arguments)
# 在函数内部定义变量时，可以用冠以global参数定义全局变量

def print_max(a,b):
    if a>b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to ', b)
    else:
        print(b, 'is maximum')

print_max(3,4)

x = 5
y = 7

print_max(x,y)