def removeDuplicate(array):
    length = len(array)
    left = 1
    for right in range(1,length):
        if array[right] != array[right-1]: 
            array[left] = array[right]
            left += 1
    for i in range(left, length):
        array[i] = 0
    return array


array = [2,3,5,5,5,7,7,11,11,13,14]
array = removeDuplicate(array)
print('New array:',array)