filename = 'full_text_small.txt'

def file_write(filename):
    with open(filename, 'r') as f:
        n = 0
        for line in f:
            n += 1
            if n <= 5:
                print(line)
        return(line)


file_write(filename)

