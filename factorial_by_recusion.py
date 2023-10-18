def factorial(n):
    """
    recusively find the factorial of a given number n

    n! = n* (n-1) * (n-2) * n(n-3) ..... 3 * 2 * 1
    There for n! = n * (n-1)!

    We know the factorial of 0 = 1 which is our base case

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
while True:
    input_str = input("please enter a number or any character to quite:")

    if input_str.isalpha():
        break

    num = int(input_str)
    result = factorial(num)
    print(str(num)+"! = " + str(result))
    