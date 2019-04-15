# 设置默认的参数值
# 默认参数值应该时不可变的，可以通过传参来指定

def say (message, times=1):
    print(message*times)

say('Hello')
say('world', 5)
