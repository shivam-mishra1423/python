# f = open('another.txt','w');
# f.write('plese write this to yhe file')
# f.close()

with open('another.txt','r') as f:
    a=f.read()
    print(a)