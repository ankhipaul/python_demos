n = int(input("no:"))
#arr = list(map(int, input().split()))
arr=[57,57, -57, 57]
largest = max(arr)
print(largest)

for i in arr[0:]:
    if largest == max(arr):
        arr.remove(max(arr))
        print(arr)

print(arr)

