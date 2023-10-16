def sequence(num):
    """
    get the n number in the sequence

    in the fibonacci sequence, we know that the first fibonacci number is 1 which is our base case

    the fibonacci number in the sequence is derived by adding the two numbers before it.
    """
    if num < 0:
        raise ValueError("Invalid input")
    
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    return sequence(num-1) + sequence(num-2)
    
numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    result = sequence(num)
    print("The "+str(num)+" number in the sequence is " + str(result))