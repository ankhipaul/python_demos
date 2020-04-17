filename = 'full_text_small.txt'
stringtomatch = 'RT @USER_'


for line in open(filename, 'r').read().split('\t'):
    if stringtomatch in line:
        string = line
        A = string.capitalize()
        #print(string[0:16])
        print(A)
