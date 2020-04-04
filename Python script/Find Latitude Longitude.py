filename = 'full_text_small.txt'
###############################
# Insert your code block here
###############################

for line in open(filename, 'r').readlines():
       string = line
       print(string[41:62])
       