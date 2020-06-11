"""
HackerRank Problem : https://www.hackerrank.com/challenges/the-minion-game/problem
Submission : https://www.hackerrank.com/challenges/the-minion-game/submissions/code/163371713
"""
def minion_game(string):
    kevin = 0
    stuart = 0
    # your code goes here
    vw = 'aeiou'.upper()
    strl = len(string)
    for i in range(strl):
        """
        Take all possible substrings, split them into two sets according to starting letter, 
        then sum elements in sets.
        If we know the starting letter, 
        we can add all substrings of different length that start with this letter.
        It will be len(s) - i
        """
        if string[i] in vw:
            kevin += strl-i
            print(kevin)
        else:
            stuart += strl -i

    if kevin == stuart:
	    print('Draw')
    elif kevin > stuart:
	    print ('Kevin %d' % kevin)
    else:
	    print ('Stuart %d' % stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)