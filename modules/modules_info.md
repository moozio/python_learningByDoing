# module

- why module
code reusing

- how to create modules
    1. create a `.py` file with including functions and varibles  

    2. implement functions in other languages and invoke them by using Python interpreter

- invoke a module
    1. `.pyc` file
    Byte-compiled file which can make import faster. If python do not have the permission of writing file in the `.py` directory, the `.pyc` file will not be created.

    2. statements
        1. `from .. import` (avoid imputing module name while invoking)
            > using `import` statement can avoid the name conflict

            ```python
            from math import sqrt
            print("Square root of 16 is", sqrt(16))
            ```

        2. `__name__` of a module
            every module has its name which can be used to make sure it is running isolated or imported.  
            case: [module_using_name.py](./module_using_name.py)  

            ```python
            if __name__ == '__main__':
                print('This program is being run by itself')
            else:
                print('I am being imported from another module')
            ```

            output:  

            ```bash
            $ python module_using_name.py
            This program is being run by itself
            $ python
            >>> import module_using_name
            I am being imported from another module
            >>>
            ```

        3. other invoking case
            can be invoked by: `from myModule import *`  
            in this case, all public name like `say_hi` will be imported. But the name `__version__` will not be imported, because it is beginning with `__`

    3. write your own modules
        case: [myModule.py](./myModule.py)
        code:  

        ```python
        def say_hi():
            print('hi')

        __version__ = '0.1'
        ```

        invoking:

        ```python
        import mymodule
        mymodule.say_hi()
        print('Version', mymodule.__version__)
        ```

        output:

        ```bash
        $ python mymodule_demo.py
        Hi, this is mymodule speaking.
        Version 0.1
        ```

    4. `dir` function
        内置的 dir() 函数能够返回由对象所定义的名称列表。 如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。该函数接受参数。 如果参数是模块名称，函数将返回这一指定模块的名称列表。 如果没有提供参数，函数将返回当前模块的名称列表。  
        code:  

        ```bash
        $ python
        >>> import sys
        # 给出 sys 模块中的属性名称
        >>> dir(sys)
        ['__displayhook__', '__doc__',
        'argv', 'builtin_module_names',
        'version', 'version_info']
        # only few entries shown here
        # 给出当前模块的属性名称
        >>> dir()
        ['__builtins__', '__doc__',
        '__name__', '__package__']
        # 创建一个新的变量 'a'
        >>> a = 5
        >>> dir()
        ['__builtins__', '__doc__', '__name__', '__package__', 'a']
        # 删除或移除一个名称
        >>> del a
        >>> dir()
        ['__builtins__', '__doc__', '__name__', '__package__']
        ```