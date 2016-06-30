def heap(array,length,strt_index):
    large_no = strt_index
    left_node_indx = (2*strt_index) + 1
    right_node_indx = (2*strt_index) + 2
    if left_node_indx < length and array[large_no] < array[left_node_indx]:
        large_no = left_node_indx
    if right_node_indx < length and array[large_no] < array[right_node_indx]:
        large_no = right_node_indx
    if large_no != strt_index:
        array[strt_index],array[large_no]=array[large_no], array[strt_index]
        heap(array,length,large_no)

def heapsort(array):
    length = len(array)
    for indx in range(length,-1,-1):
        heap(array,length,indx)
    for indx in range(length-1,0,-1):
        array[indx], array[0] = array[0], array[indx]
        heap(array,indx,0)

input = raw_input("enter the numbers to be sorted separated by ','")
array = [int(val) for val in input.split(",")]
heapsort(array)
print array
