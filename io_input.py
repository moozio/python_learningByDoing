def reverse(text):
    return text[::-1] # 切片slicing

def is_palindrome(text):
    return text == reverse(text)

something = input("enter text: ")
if is_palindrome(something):
    print("palindrome")
else:
    print("not palindrome")