"""
HackerRank Problem: https://www.hackerrank.com/challenges/piling-up/problem
Submission : https://www.hackerrank.com/challenges/piling-up/submissions/code/163371320
"""
for t in range(int(input())):
    ln = int(input())
    lst = list(map(int, input().split()))
    i = 0
    """
    Keep checking the elements from the left side.
    It has to be greater than the next element in order to pile up.
    The element in the middle should be the least. 
    """
    while i < ln - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < ln - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == ln - 1 else "No")