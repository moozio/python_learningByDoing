# if-else
num = 23
guess = int(input("Enter an integer: "))
# get user input by input()

# remember the : for reminding the following code blocks
if guess == num:
    print("you get it!")
elif guess > num:
    print("it's a little higher than that")
else:
    print("it's a little lower than that")

print("done")

# python 没有switch语句
# 只能使用if-else
# 但可以通过 字典 来加速完成