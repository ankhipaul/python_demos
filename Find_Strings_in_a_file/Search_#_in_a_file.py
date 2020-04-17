filename = 'full_text_small.txt'

# results =[]
###############################
# Insert your code block here
###############################
with open(filename, 'r') as f:
    for line in f.readlines():
       if '#' in line:
           candidates = line.split('#')
           for c in candidates[1:]:
               print(c.split(' ')[0].rstrip('\n'))
f.close()

