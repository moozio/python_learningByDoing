# general info for python

## process of software development

>Software is grown, not built

- phases of software development
    1. what (demand analysis)
    2. how (design)
    3. do it (implementation)
    4. test (test and bug fixing)
    5. use (operations or development)
    6. maintain (improving)

## Object-orient programming

>类与对象是面向对象编程的两个主要方面。一个类(Class)能够创建一种新的类型(Type)，其中对象(Object)就是类的实例(Instance)。

- general info  

  - 属于某个对象或类的变量被称作字段(Field)  
  - 类的函数称为方法(method)  
  - 字段与方法都可以看作其所属的类的属性(Attribute)  
  - 字段有两种类型,实例变量(Instance Variables)与类变量(Class Variables)

### `self` -- 引用对象本身的特定变量引用

如果你有一个没有参数的功能，你依旧必须拥有一个参数: `self`

### 类 class

- general info:
    example:  

    ```python
    class Person:
        def say_hi(self):
            print('hello, how are you?')

    p = Person()
    p.say_hi() # = Person().say_hi()
    ```

- `__init__`方法
  
  - `__init__`会在对象被实例化时立即运行，将进行操作的目标对象进行初始化操作。example:

    ```python
    class Person:
        def __init__(self, name):
         self.name = name
        def say_hi(self):
          print('Hello, my name is', self.name)

    p = Person('Swaroop')
    p.say_hi()
    # 前面两行同时也能写作
    # Person('Swaroop').say_hi()
    ```

### 类变量与对象变量

- general info
  
  - 字段field: 绑定到对象namespace的普通变量，仅在对象存在的context中有效。包含类变量和对象变量。
  - 类变量class variable: 共享的，可以被属于该类的所有实例访问。只有一个副本，一个变了其他所有实例都会变。
  - 对象变量object variable: 类的每一个独立对象或实例拥有。
  - code: [opp_objvar.py](./opp_objvar.py)
  - 个人总结：
    >python的OO与java不同，class可以被单独访问，有自己属性和方法(方法需要`@classmethod`装饰)。class中的方法声明时默认是对象变量，默认(隐式)包含参数`self`(第一个参数)，指向对象自身。只能使用 `self` 来引用同一对象的变量与方法.**类变量是各对象共享的**，通过 `className.methodName` 或 `className.variableName` 调用。
  - 类成员的访问权限
    所有的类成员都是公开的,但有一个例外：如果你使用数据成员并在其名字中使用**双下划线作为前缀**，形成诸如 `__privatervar` 这样的形式，Python 会使用名称调整(Namemangling)来使其有效地成为一个私有变量  
    所有类成员(包括数据成员)都是公开的，并且 Python 中所有的方法都是虚拟的(Vireual)
  - 包装器 wrapper
    - `@classmethod`装饰器等价于`how_many = classmethod(how_many)`

- 继承 inheritance

  - 父类(基类base class/超类 super class)
  - 子类(派生类 derived class)
  - example: [opp_subclass.py](./opp_subclass.py)
  - 个人总结：
    - python的继承与java不同
    - 通过 `class subclassName(superclassName):` 声明继承关系(在定义类时我们需要在类后面跟一个包含基类名称的元组)。
    - 方法的继承通过在子类的方法声明中直接调用父类的对应方法并传入参数实现。重写父类方法则是不调用父类方法，直接在子类中实现事务逻辑。**如果在子类中定义了`__init__`方法，python则不会自动调用基类的构造函数，必须在子类中显式调用**，相反，**如果子类中没有定义`__init__`方法，python会自动调用基类的构造函数**。
    - python总会从当前的十记类型中寻找方法，如果没有找到，则向所属基本类中依顺序查找。
    - 继承元组(inheritance tuple)中超过了一个类，则称多重继承(multiple inheritance)