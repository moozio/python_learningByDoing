# Exceptions and Handling

## exception

nothing important

## exception handling

> use `try...except` for handling exceptions

- example:  

    ```python
    try:
        text = input("Enter something...")
    except EOFError:
        print('why did you do an EOF on me')
    except KeyboardInterrupt:
        print('You can cancel the operation')
    else:
        print('you entered {}'.format(text))
    ```

- how it works:

>将所有可能引发异常或错误的语句放在 `try` 代码块中，并将相应的错误或异常的处理器(Handler)放在 `except` 子句或代码块中。 `except` 子句可以处理某种特定的错误或异常，或者是一个在括号中列出的错误或异常。如果没有提供错误或异常的名称，它将处理所有错误与异常

>如果没有任何错误或异常被处理，那么将调用 Python 默认处理器，它只会终端程序执行并打印出错误信息。我们已经在前面的章节里见过了这种处理方式。你还可以拥有一个 `else` 子句与 `try..except` 代码块相关联。 `else` 子句将在没有发生异常的时候执行。

## throw exception

> use `raise` statements to trigger an exception. 需提供错误名或异常名以及抛出异常的对象

example: [exceptions_raise.py](./exceptions_raise.py)

## `try...finally`

>无论是否发生`exception`, `finally`内的代码都执行

example: [exception_finally.py](./exception_finally.py)

> 在`print`之后使用`sys.stout.flush()`可以让`print`的内容立即打印到屏幕

## `with` 语句

> 使 `try...finally` 的资源获取释放过程以更干净的姿态完成

- example:  

    ```python
    with open("poem.txt") as f:
        for line in f:
            print(line, end='')
    ```

- how it works
    `with` 语句会自动获取 `open` 的返回对象，本例为 `theFile`  
    它总会在代码块开始前调用 `theFile.__enter__` 函数，并总会在代码执行完毕后调用 `theFile.__exit__`  
    避免显示调用 `try...finally`