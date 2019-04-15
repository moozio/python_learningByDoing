# keyword argument
# 对参数命名，传参的时候也可以通过命名参数来传递，可以忽略参数顺序

def func(a, b=10, c=100):
    print('a=',a,' ,b=',b,' ,c=',c)

func(3,7)
func(25, c=24)
func(c=50, b=60, a=1)