# input and output

## use `input()` to get user input

example: [io_input.py](./io_input.py)

## input from file

functions including: `read`, `readline`, `write` and etc.  
After finishing reading, invoke `close` to finish. example: [io_using_file.py](./io_using_file.py)

## `pickle`

>Python 提供了一个叫作 `Pickle` 的标准模块，通过它你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回。这叫作持久地(Persistently)存储对象。  

example: [io_pickle.py](./io_pickle.py)  

how it workds:  
>要想将一个对象存储到一个文件中，我们首先需要通过 `open` 以写入(write)二进制(binary)模式打开文件，然后调用 `pickle` 模块的 `dump` 函数。这一过程被称作封装(Pickling)，接着，我们通过 `pickle` 模块的 `load` 函数接收返回的对象。这个过程被称作拆封
(Unpickling)。

## Unicode

>当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们的 `Unicode` 字符串转换至一个能够被发送和接收的格式，这个格式叫作 `UTF-8`。  

example:  

```python
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()

print(text)
```

how it works:  
> `io.open` 并提供了“编码(Encoding)”与“解码(Decoding)”参数来告诉 `Python` 我们正在使用 `Unicode`。