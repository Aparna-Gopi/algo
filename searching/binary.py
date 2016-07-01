def binary(array,number):
    mid = len(array)//2
    if array[mid] == number:
        return mid
    elif number < array[mid]:
        array = array[:mid]
        return binary(array,number)
    else:
        array = array[mid:]
        return mid+binary(array,number)

array = input("enter a list of numbers")
array.sort()
number = input("enter a number")
result = binary(array,number)
print result
