def partition(array,strt_indx,end_indx):
    indx1 = strt_indx - 1
    pivot = array[end_indx]
    for indx2 in range(strt_indx,end_indx):
        if array[indx2] <= pivot:
            indx1 +=1
            array[indx1], array[indx2] = array[indx2], array[indx1]
    array[indx1+1], array[end_indx] = array[end_indx], array[indx1+1]
    return (indx1+1)

def quicksort(array,strt_indx,end_indx):
    if strt_indx < end_indx:
        pivot = partition(array,strt_indx,end_indx)
        quicksort(array,strt_indx,pivot-1)
        quicksort(array,pivot+1,end_indx)

input = raw_input("enter the numbers to be sorted separated by ','")
array = [int(val) for val in input.split(",")]
quicksort(array,0,len(array)-1)
print array
