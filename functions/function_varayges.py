# 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数(Positional Arguments)都将被收集并汇集成一个称为“param”的元组(Tuple)。
# 当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典(Dictionary)

# 自动判断时字典类型还是元组类型

def total(a=5, *numbers, **phonebook):
    print('a=',a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1,2,3, Jack=123, Hohn=456, Ng=789))