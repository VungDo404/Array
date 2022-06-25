def permute(array, permutation):
    length = len(array)
    for i in range(length):
        while i != permutation[i]:
            swapIndex = permutation[i]
            array[i], array[swapIndex] = array[swapIndex],array[i]
            permutation[i], permutation[swapIndex] = permutation[swapIndex],permutation[i]
    return