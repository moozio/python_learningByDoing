# plus
print(3+5)
print("'a' + 'b' = " +'a' + 'b')

# minus
print(50-20) #30

# times
print(3*5) #15
# this is very convenient for operating string
print('la'*3) # 'lalala'

# power
print (3**5) # 3*3*3*3*3 = 243

# divide
print(12/7) # 1.7142857142

# aliquot
print(13//3) # 13//3 = 4
print(-13//3) # -13//3 = -5

# mod
print(13%3) # 13%3 = 1
print(-25.5%2.25) # = 1.5 (2.25*(-12) = -27)

# shift
print(2<<2) # 8
print(9>>2) # 2 

# logic AND
n = 1024
print (n&(n-1)) # 0
print(n&(n+1)) # 1024

# logic OR 
print(3|4) # 3|4 = 11 | 100 = 111 = 7
print(5|3) # 5|3 = 101 | 11 = 111 = 7

# logic XOR (eXclusive OR)
print(5^3) # 5^3 = 101 ^ 11 = 110 = 6

# logic NOT
print(~5) # -6
# reason: two's complete
# 5 = 0101
# in two's complete: ~5 = inverse(0101) + 1 = 1010 + 1 = 1011 = -6
# why -6: by the definition of two's complete, ~x = -(x+1)

# less than / larger than / no larger than/ no less than/ is equal
print(1 > 2)
print(2 > 1)

# boolean NOT
x = True
y = False
print (not x)
print (not y)

# boolean AND
print(x and y)

# boolean OR
print(x or y)