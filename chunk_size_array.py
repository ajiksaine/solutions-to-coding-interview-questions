# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

def chunk_size_array(my_list,length):
    """
    Divide a given array into sub arrays of size length

    starting at position 0 split the array at (position +  length)
    then set the new position to (position + length) and  keep spliting the array to the end

    """
    result = []
    position = 0
    current = position + length

    while current <= len(my_list):
        result.append(my_list[position:current])
        position = current
        current = position + length
    if position < len(my_list):
        result.append(my_list[position:len(my_list)])

    return result

while True:

    input_str = input("Please enter you array values seperated by space (or exit to quit):")
    if str(input_str) == "exit":
        break
    input_list = [int(x) for x in input_str.split()]

    # Get user input for the target element
    chunck_size = input("Enter chunk size: ")

    length = int(chunck_size)
    
    print(chunk_size_array(input_list,length))
