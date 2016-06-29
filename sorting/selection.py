input = raw_input("enter the numbers to be sorted separated by ','")
array = [int(val) for val in input.split(",")]
length_arr = len(array)
for indx in range(0,length_arr):
    curr_min_indx = indx
    for curr_indx in range(indx+1, length_arr):
        if array[curr_min_indx] > array[curr_indx]:
            curr_min_indx = curr_indx
    array[indx], array[curr_min_indx] = array[curr_min_indx], array[indx]
print array
