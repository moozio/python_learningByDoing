# more information about Python

## pass tuple

for returning multiple value from a function.

- example:

    ```bash
    >>> def get_error_details():
    ... return (2, 'details')
    ...
    >>> errnum, errstr = get_error_details()
    >>> errnum
    2
    >>> errstr
    'details'
    ```

- how it works
    返回的结果是一个具有n元的元组  
    在python中减缓两个值的最快速方式：`a, b = b, a`

## special mehtods

> 特殊方法用来模拟内置类型的某些行为。

- examples:
    1. `__init__(self, ...)` 这一方法在新创建的对象被返回准备使用时被调用。
    2. `__del__(self)` 这一方法在对象被删除之前调用（它的使用时机不可预测，所以避免使用它）
    3. `__str__(self)` 当我们使用 `print` 函数时，或 `str()` 被使用时就会被调用。
    4. `__lt__(self, other)` 当小于运算符`<`被使用时被调用。类似地，使用其它所有运算符`+`、`>` 等等时都会有特殊方法被调用。
    5. `__getitem__(self, key)` 使用 `x[key]` 索引操作时会被调用。
    6. `__len__(self)` 当针对序列对象使用内置 `len()` 函数时会被调用

## single statement block

## `Lambda` 表格

> `lambda` 语句可以创建一个新的函数对象。从本质上说， `lambda` 需要一个参数，后跟一个表达式作为函数体，这一表达式执行的值将作为这个新函数的返回值

- example: [more_lambda.py](./more_lambda.py)

    ```python
    points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
    points.sort(key=lambda i: i['y'])
    print(points)
    ```

## list comprehension (列表推导)

> 用于从一份现有的列表中得到一份新列表

- exmaple:

    ```python
    listOne = [2, 3, 4]
    listTwo = [2*i for i in listOne if i > 2]
    print(listTwo)
    ```

- output

    ```bash
    [6, 8]
    ```

- 意义
当我们使用循环来处理列表中的每个元素并将其存储到新的列表中时时，它能减少样板（Boilerplate）代码的数量。

## 在函数中接收元组喝字典

> 有一种特殊方法，即分别使用 `*` 或 `**` 作为元组或字典的前缀，来使它们作为一个参数为函数所接收。当函数需要一个可变数量的实参时，这将颇为有用。

- example:

    ```python
    >>> def powersum(power, *args):
    ...     '''Return the sum of each argument raised to the specified power.'''
    ...     total = 0
    ...     for i in args:
    ...         total += pow(i, power)
    ...     return total
    ...
    # 对第二个到最后一个参数求其乘方，指数为第一个数
    >>> powersum(2, 3, 4)
    25
    >>> powersum(2, 10)
    100
    ```

- how it works

    > 在 `args` 变量前添加了一个 `*` 前缀，函数的所有其它的额外参数都将传递到 `args` 中，并作为一个元组予以储存
    > 如果采用的是 `**` 前缀，则额外的参数将被视为字典的键值—值配对

## `assert` 断言

`assert` 语句用以断言(Assert)某事是真的，并想确认这一点，如果不是真的就抛出一个错误。断言失败将抛出 `AssertionError`

- example:

    ```python
    >>> mylist = ['item']
    >>> assert len(mylist) >= 1
    >>> mylist.pop()
    'item'
    >>> assert len(mylist) >= 1
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AssertionError
    ```

## `decorators` 装饰器

>应用包装函数的快捷方式。这有助于将某一功能与一些代码一遍又一遍地“包装”。

- example:

    >举个例子，我为自己创建了一个 `retry` 装饰器，这样我可以将其运用到任何函数之中，如果在一次运行中抛出了任何错误，它就会尝试重新运行，直到最大次数 `5` 次，并且每次运行期间都会有一定的延迟。这对于你在对一台远程计算机进行网络调用的情况十分有用：[retry.py](./retry.py)
