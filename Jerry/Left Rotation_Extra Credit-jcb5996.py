def leftRotation():
    numbers = []  #input method inspired by link: https://www.kite.com/python/answers/how-to-extract-integers-from-a-string-in-python
    values = input()
    for string in values.split():  #reads each string separated by spaces
        if string.isdigit():  #checks if string is an integer
            numbers.append(int(string))
            
    if len(numbers)<2:  #error message if not a valid input
        return "Error. Not enough inputs"
    
    length = numbers[0]  #records length of array as first entry
    rotation = numbers[1]  #records the rotation amount as second entry
    
    r = rotation % length  #accounts for any full-rotations
    array = [i+1 for i in range(length)]
    return array[r:]+array[:r]  #quick method to rotate items

print(leftRotation())
