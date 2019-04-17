# encoding = UTF-8

class ShortInputException(Exception):
    '''an exception class defined by user'''
    def __init__(self, length, atLeast):
        Exception.__init__(self)
        self.length = length
        self.atLeast = atLeast

try:
    text = input('Enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('why did you do an EOF on me')
except ShortInputException as ex:
    print(('ShortInputException: the input was ' 
        + '{0} long, excepted at least {1}')
        .format(ex.length(), ex.atLeast))
else:
    print('No exception was raised')