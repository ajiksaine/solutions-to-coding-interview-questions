def search_in_rotated_list(list,key,low,high):
    """
    Binary search to find the target value in the list where list can be rotated n number of times
    find the smallest value in the list
    BASE CASE
    if low > high

    RECUSIVE CASE
    check if list[mid] is grater than list[high], then the left is sorted and the right is not
    else if list[mid] is less than list[high], then the right is sorted and the left is not

    for the case where the left is sorted: if the key falls between the value at low and the value at mid point,
    then  move left, otherwise move right
    for the case where the right is sorted: if the key falls between the value at mid and the value at high,
    then move right, otherwise move left
    """

    if low > high:
        return None
    
    mid = (low + high)//2

    if list[mid] == key:
        return mid
    
    if list[mid] > list[high]:
        if key > list [low] and key < list[mid]:
            return search_in_rotated_list(list,key,low,mid-1)
        else:
            return search_in_rotated_list(list,key,mid+1,high)
    else:
        if key > list[mid] and key <= list[high]:
            return search_in_rotated_list(list,key,mid+1,high)
        else:
            return search_in_rotated_list(list,key,low,mid-1)
        
        

def verify(key,result):
    if result is not None:
        print(f"{key} found at position: {result}")
    else:
        print(f"{key} not in the given list")



# Get user input for the sorted array
input_str = input("Enter a sorted array of numbers, separated by spaces: ")
input_list = [int(x) for x in input_str.split()]



while True:
    # Get user input for the target element
    target = input("Enter the target element to search for (or -1 to quit): ")

    if str(target) == "exit":
        break

    key = int(target)
    
    verify(key,search_in_rotated_list(input_list,key,0,len(input_list)-1))



    
    
       