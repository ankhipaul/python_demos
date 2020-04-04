filename = 'full_text_small.txt'
stringtomatch = 'RT @USER_'

# results =[]
###############################
# Insert your code block here
###############################
# with open(filename, 'r') as a:
# for line in a:
for line in open(filename, 'r').read().split('\t'):
    if stringtomatch in line:
        string = line
        A = string.capitalize()
        #print(string[0:16])
        print(A)
