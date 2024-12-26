lis1=[1,2,3,4]
lis2=[3,4,5,6]
lis3=[]
for ele in lis1:
    if ele in lis2:
        lis3.append(ele)
print(lis3)

''' lis3=list(set(lis1) & set(lis2))
    print(lis3'''
