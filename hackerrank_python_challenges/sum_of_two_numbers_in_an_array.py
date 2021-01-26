# Python program to find if there are
# two elements add upto a given sum

# function to check for the given sum in the array
def printsum(arr, arr_size, tot):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = tot - arr[i]
        if (temp in s):
            print("Pair with given sum " + str(tot) +" is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])


if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, 8]
    sum1 = 16
    printsum(arr, len(arr), sum1)

