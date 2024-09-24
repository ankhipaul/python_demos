"""
Given an array of few people. We need to partner them in such a way so that the difference between them is minimum.
Then find the sum of those differences.

Function minimumBias has one input parameter-
arr: an array of integers

Input Format
The first line contains an integer denoting , the number of people in the array .
The second line describes as integers representing the person.

Constraint
n has to be a multiple of 2 in order to create pairs

Output Format
Integer : Sum of the differences of each group of partners

Sample Input
n = 6
arr = [2,5,4,8,6,1]

Sample Output
4

Explanation
2 should be paired with 1 as the minimum difference is 1.
5 should be paired with 4 as the minimum difference is 1.
Similarly, 8 should be paired with 6.

Sum of the differences = 1+1+2 ,Hence 4
"""
import numpy as np

def minimumBias(arr):
    #Sorting the array to bring the numbers closer
    arr.sort()

    #As pairing is required, length of array will always be multiple of 2
    div = int(len(arr) / 2)

    cnt = 0

    #Using numpy to split the sorted array
    sub_arr = np.array_split(arr,div)

    #Iterating over each sub-arrays
    for i in list(sub_arr):

        #Using enumerate to compare the next element of the array with the current one
        for j,k in enumerate(i[:-1]):
            diff = i[j+1] - k
            cnt += diff
    return cnt

if __name__ == '__main__':
    t = int(input())
    arr = []

    for t_itr in range(t):
        n = int(input())
        arr.append(n)

    bias = minimumBias(arr)
    print(bias)
