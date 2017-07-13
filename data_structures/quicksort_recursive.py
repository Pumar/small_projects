def quicksort(array):
    pivot = -1
    i=0
    while (len(array)+pivot)>i:
        if array[pivot] < array[i]:
            temp = array[pivot]
            array[pivot] = array[i]
            array[i] = array[pivot-1]
            array[pivot-1] = temp
            pivot-=1
        else:         
            i+=1
    if len(array)>2:
        array[:pivot] = quicksort(array[:pivot])
        array[pivot:] = quicksort(array[pivot:])
    return array

print (quicksort([1,5,7,12,5,8,0]))