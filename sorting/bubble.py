input = raw_input("enter the numbers to be sorted separated by ','")
input_array = [int(val) for val in input.split(",")]
for indx in range(len(input_array)):
	for curr_indx in range(0,len(input_array)-1):
		if input_array[curr_indx] > input_array[indx]:
			input_array[curr_indx], input_array[indx] = input_array[indx], input_array[curr_indx]
print input_array
