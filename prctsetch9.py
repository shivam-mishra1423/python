#Q1
# f =open('poems.txt')
# t=f.read()
# if 'twinke' in t:
#     print("twinkel is present")
# else:
#     print("twinkel is not present")
#     f.close()

#Q3
for i in range(2,21):
    with open(f"tables/multiplication_table_of_{i}",'w') as f:
        for j in range(1,11):
           f.write(f"{i}X{j}={i*j}\n")
    break
                
