#!/bin/python3
'''
hackerrank problem
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''

from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine) == {}:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    magazine = input().rstrip().split()

    note = input().rstrip().split()

    a = checkMagazine(magazine, note)

    print(a)
