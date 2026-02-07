def factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num-=1
    return factorial
num=int(input("Enter a number: "))
print(f"factorial of {num} is {factorial(num)}")