input_array = input("enter a list of items")
length = len(input_array)
number = input("enter the number")
for indx in range(length):
    if input_array[indx] == number :
        print "the position of the given number is "
        print indx
