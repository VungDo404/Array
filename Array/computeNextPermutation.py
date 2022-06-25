# Given [1,4,7,9,0] the next permutation will be [1,4,9,0,7] 
# The largest number from those 5 digits is [9,7,4,1,0] and the smallest is [0,1,4,7,9] --> It's clearly that if all the digits are in decreasing order (from left to right) then we have the biggest and vice versa  
# We can say that the more decreasing (from LTR) our numbers are the bigger they become
# Firstly, [1,4,7,9,0] we find where the number that not in increasing order (from right to left), in this case it's digit 7 
# We swap it with the next least significant number, that number certainly larger than 7 --> we obtain [1,4,9,7,0]
# Compare the result we've obtained with the expected result, we need to do some other things. We want the next permutation to be the smallest number that larger than the given input. Knowing that, now every number in the left of the number we've swapped is in decreasing order (from left to right). Thus to obtain the smallest result we just need to reverse them --> [1,4,9,0,7] 
# Read more on EPI

## Coding section
def nextPermutation(input):
    # find the non increasing number and swap it
    i = len(input)-1
    while i >=0:
        if (input[i] > input[i-1]):
            input[i], input[i-1] = input[i-1], input[i]
            break
        i-=1
    if i == 0: return False
    # reverse 
    input = input[0:i] + input[len(input)-1:i-1:-1]
    return input


print(nextPermutation([9,7,4,1,0]))