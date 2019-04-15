num = 23
running = True 

while running:
    guess = int(input("enter an integer"))

    if guess == num:
        print("you got it!")
        running = False
    elif guess>num:
        print("larger")
    else:
        print("lower")
# else:
#     print("the while loop is over")
    
print("done")

# python 中可以在 while 循环后用else语句