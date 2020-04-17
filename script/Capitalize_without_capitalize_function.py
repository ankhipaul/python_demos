s = 'hello world'
y =[]
for i in s.split(' '):
    x=i[0].upper() + i[1:]
    y.append(x)
z= ' '.join(y)
print(z)
