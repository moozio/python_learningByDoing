# data structure in python

- basic info -- 4 build-in data structures
    1. `list` -- 有序项目的集合
        > 字段(field): 它是只为该类定义且只为该类所用的变量  

        list example:  
        `shoplist = ['apple', 'mango', 'carrot', 'banana']`

        `list`通过`for items in listName`进行遍历。通过`listName.append(stringName)`进行添加。通过`del listName[index]`进行删除。
    2. `tuple`元组 -- 用于将多个对象保存到一起(元组时不可变的，不可编辑或更改)
        tuple example:  
            1. normal: `zoo = ('python', 'elephant', 'penguin')`  
            2. with 0 elements: `myempty = ()`  
            3. with only 1 element: `singleton = (2,)`. 必须要在第一个元素后加上一个`,`。
        methods: `len(tupleName)`, `tupleName[index]`

    3. `dictionary`字典 -- 键值对
        只能使用不可变的对象（如字符串）作为字典的键值。字典不会以任何方式进行排序。  
        example:  
        `d = {key : value1 , key2 : value2}`

        ```python
        # “ab”是地址（Address）簿（Book）的缩写
        ab = {
            'Swaroop': 'swaroop@swaroopch.com',
            'Larry': 'larry@wall.org',
            'Matsumoto': 'matz@ruby-lang.org',
            'Spammer': 'spammer@hotmail.com'
        }

        print("Swaroop's address is", ab['Swaroop'])

        # 删除一对键值—值配对
        del ab['Spammer']
        print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

        for name, address in ab.items():
            print('Contact {} at {}'.format(name, address))

        # 添加一对键值—值配对
        ab['Guido'] = 'guido@python.org'

        if 'Guido' in ab:
            print("\nGuido's address is", ab['Guido'])
        ```

        通过字典的`item()`方法访问每一组键值对。

        - 序列 Sequence
            >列表、元组和字符串可以看作序列(Sequence)的某种表现形式。
            >序列的主要功能是资格测试(Membership Test)(也就是 in 与 not in 表达式)和索引操作(Indexing Operations)，它们能够允许我们直接获取序列中的特定项目。

            切片 slicing

            ```python
            shoplist = ['apple', 'mango', 'carrot', 'banana']
            name = 'swaroop'
            # Indexing or 'Subscription' operation #
            # 索引或“下标（Subcription）”操作符 #
            print('Item 0 is', shoplist[0]) # apple
            print('Item 1 is', shoplist[1]) # mango
            print('Item 2 is', shoplist[2]) # carroy
            print('Item 3 is', shoplist[3]) # banana
            print('Item -1 is', shoplist[-1]) # banana
            print('Item -2 is', shoplist[-2]) # carrot
            print('Character 0 is', name[0]) # s
            # Slicing on a list #
            print('Item 1 to 3 is', shoplist[1:3]) # ['mango', 'carrot']
            print('Item 2 to end is', shoplist[2:]) # ['carrot', 'banana']
            print('Item 1 to -1 is', shoplist[1:-1]) # ['mango', 'carrot']
            print('Item start to end is', shoplist[:])
            # 从某一字符串中切片 #
            print('characters 1 to 3 is', name[1:3]) # wa
            print('characters 2 to end is', name[2:]) # aroop
            print('characters 1 to -1 is', name[1:-1]) # waroo
            print('characters start to end is', name[:])

            # shoplist[::-1] -> ['banana', 'carrot', 'mango', 'apple']
            # shoplist[::3] -> ['apple', 'banana']
            ```

    4. `set`集合 -- 简单对象的无序集合

        ```bash
        >>> bri = set(['brazil', 'russia', 'india'])
        >>> 'india' in bri
        True
        >>> 'usa' in bri
        False
        >>> bric = bri.copy()
        >>> bric.add('china')
        >>> bric.issuperset(bri)
        True
        >>> bri.remove('russia')
        >>> bri & bric # OR bri.intersection(bric)
        {'brazil', 'india'}
        ```

- something more about string
    code:

    ```python
    # 这是一个字符串对象
    name = 'Swaroop'
    if name.startswith('Swa'):
        print('Yes, the string starts with "Swa"')

    if 'a' in name:
        print('Yes, it contains the string "a"')

    if name.find('war') != -1:
        print('Yes, it contains the string "war"')

    delimiter = '_*_'
    mylist = ['Brazil', 'Russia', 'India', 'China']
    print(delimiter.join(mylist)) # Brazil_*_Russia_*_India_*_China
    ```