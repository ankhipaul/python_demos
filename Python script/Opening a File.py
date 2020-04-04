f1 = 'full_text_small.txt'
with open(f1, 'r') as f:
    n = 0
    for line in f:
        n+=1
        if(n<4):
            print(line)