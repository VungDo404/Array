class minHeap: 
    def __init__(self, val=0): 
        self.val = val 
        self.left = None 
        self.right = None
        
def heapify(array):
    length = len(array)
    for i in range(length):
        if 2*i+1 < length-1: 
            if array[i] > array[2*i+1]: 
                array[i], array[2*i+1] = array[2*i+1], array[i]
        if 2*i+2 < length-1: 
            if array[i] > array[2*i+2]: 
                array[i], array[2*i+2] = array[2*i+2], array[i]
        parent = child = i 
        while (parent -1)/2 >= 0 and array[(parent -1)//2] > array[child]: 
            array[child],array[(parent -1)//2] = array[(parent -1)//2],array[child]
            parent = (parent -1)//2
    return array

        
array = [5, 7, 9, 1, 3]
array = heapify(array)
print(array)
        