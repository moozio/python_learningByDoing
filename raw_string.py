# raw string (without processing like escape)
print(r"Newlines are indicated by \n")

# encoding of string
# from Unicode to Bytes (for transforming via the Internet or saving into a file)
c = b'abc' # c storing bytes
print(c)

cn = '中文'  # type = string, unicode
en = 'ABC'   # type = string, unicode
print(cn.encode('utf-8')) # type = bytes
print(en.encode('ascii')) # type = bytes

# from Bytes to Unicode/UTF-8/ASCII (handling stream from file or internet)
cn_byte = b'\xe4\xb8\xad\xe6\x96\x87'
en_byte = b'ABC'
print(en_byte.decode('unicode_escape'))
print(cn_byte.decode('utf-8'))
print(en_byte.decode('ascii'))