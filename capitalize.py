# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.

def capitalize(str):
    """
    Loop through the characters in the string and capitalize the begining of each word.
    After every space it sees, it turn the next charater to uppercase
    """
    result = ''
    current_space = True

    for i in range(0,len(str)):
        
        if current_space is True:
            result += str[i].upper()
            current_space = False
        else:
            if str[i] == ' ':
                current_space = True
            result += str[i]
    return result


while True:
    input_str = input("Enter a Sentence or a phrase: ")

    if str(input_str) == "exit":
        break
    
    print(capitalize(input_str))
