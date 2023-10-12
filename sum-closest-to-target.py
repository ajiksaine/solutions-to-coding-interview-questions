"""
QUESTIONS
Given two different array find the sum of two numbers from both arrays that is closest to the target
eg [-1,3,8,2,9,5] and [4,1,2,10,5,20] and the target is 24
"""

def closestbrutforce(first_list, second_list, target):
    """
    loop throught the first array and for each value sum each value of the second array
    compare with the previous smallest value until the end of the arrays
    """
    closest = []


    for first_num in first_list:
        for second_num in second_list:
            sum_num = first_num + second_num
            if len(closest) == 0 or abs(target - sum_num) < abs (target-(closest[0][0]+closest[0][1])):
                closest = [(first_num,second_num)]
            elif abs(target - sum_num) == abs (target-(closest[0][0]+closest[0][1])):
                closest.append((first_num,second_num))

    return closest


# Get user input for the sorted array
first_input_str = input("Enter a array of numbers, separated by spaces for the first list: ")
first_input_list = [int(x) for x in first_input_str.split()]

second_input_str = input("Enter a array of numbers, separated by spaces for the first list: ")
second_input_list = [int(x) for x in second_input_str.split()]

while True:
    # Get user input for the target element to search
    target = input("Enter the target element to search for (or exit to quit): ")

    if str(target) == "exit":
        break

    key = int(target)

    print(closestbrutforce(first_input_list,second_input_list,key))