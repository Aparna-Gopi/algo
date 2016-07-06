a = raw_input()
a = a.split(",")
arr = [int(x) for x in a]
for i in range(1,len(arr)) :
	for j in range(i-1, -1, -1) :
		if arr[j] > arr[i]:
			arr[j], arr[i] = arr[i], arr[j]
			i = i-1
print arr
