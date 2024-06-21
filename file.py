#use open function to read the content of file! 
f=open('simple.txt','r')
data = f.read(5)#print first five char
print(data)
f.close()

#readlinefunction
# f=open('simple.txt','r')
# data = f.readline()
# print(data)
# f.close()