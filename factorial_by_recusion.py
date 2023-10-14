def factorial(n):
    """
    recusively find the factorial of a given number n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

numbers = [1,2,3,4,5,6]

for num in numbers:
    result = factorial(num)
    print(str(num)+"! = " + str(result))
