def smallest(list,low,high):
    """
    Find the smallest in the list given a rotated sorted list
    """
    if len(list) <= 0:
        return None
    
    mid = (low+high)//2
    
    if list[mid]  < list[mid-1]:
        return mid
    elif list[mid] > list[mid+1]:
        return mid+1
    elif mid < high:
        return smallest(list,low,mid-1)
    else:
        return smallest(list,mid+1,high)
        

def verify(result):
    if result is not None:
        print(f"The smallest value in the list is: {result}")
    else:
        print("The list is empty")



while True:
    # Get user input for the sorted array
    input_str = input("Enter a sorted array of numbers, separated by spaces or -1 to quite: ")

    if input_str  == "exit":
        break

    input_list = [int(x) for x in input_str.split()]
    
    

    verify(smallest(input_list,0,len(input_list)-1))