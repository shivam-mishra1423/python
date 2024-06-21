#Q1
# num =int(input("enter the number : "))
# for i in range(1,11):
#     print(str(num) +   "X"  +  str(i) + "=" + str(i*num))

#Q2
# l1={"HArry","Sohan","Sachin","Rahul"}

# for name in l1:
#     if name.startswith("S"):
#      print("hello" + " "+name)

# Q3 prime number or not
# num=int(input("enter the number  :"))
# prime=True
# for i in range(2, num): 
#     if(num%i==0):
#      prime=False
#      break
# if prime:
#         print("this number is prime : ")
# else:
#     print("this number is not prime : ")
     
# #Q6
# num=int(input("enter a number : "))
# factorial = 1
# for i in range(1,num+1):
#     factorial=factorial * i
# print(f"the factorial of this  number is{factorial}")
    
#Q8
# n=4 
# for i in range(4):
#     print("*" * (i+1))

#Q7
n=4
for i in range(3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))


      