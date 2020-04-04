file_name = 'full_text_small.txt'
with open(file_name,'r') as f:
    reading=f.readlines()
    print(type(reading))
    print(reading[2:])