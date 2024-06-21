#Q1
# def maximum(num1, num2, num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
  
  
  #Q2     
# m =maximum(3, 5, 234)
# print("the value of the maximum is " +str(m))

# def farh(cel):
#     return (cel * (9/5)) + 32
# c = 45
# f= farh(c)
# print("fahreheit temperature is " +str(f))


#Q5
# n  = 3
# for i in range(n):
#     print("*" * (n-i))

#Q6
def remove_and_strip(string):
    newstr = string.replace(word, "")
    return newstr.strip()
    
this = "    harry is good     "
n = remove_and_strip(this, "harry")
print(n)