def fizz_buzz():
    """
    Write a program that prints a number from 1 to 100. But for Multiples of 3, print "Fizz" instead of the number and for multiples of 5 
    print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz"

    input= array of numbers eg. [1,2,3 ....... 100]
    output = print statement of numbers, Fizz, Buzz or FizzBuzz

    STEPS
    1 Define array of numbers from 1 to 100
    2 loop through the array to the end
    3 check if the number is a multiple of 3 and 5 return FizzBuzz
    5 check if the number is a multiple of only 3 return Fizz
    6 if the number is also a multiple of only 5 by return Buzz 
    7 else return the number
    """
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()