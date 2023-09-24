lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
s1=lst[5:15] 
s2=lst[::4] 
sum=avg=0 
print("Slice1") 
for a in s1: 
    sum+=a 
    print(a,'',end='') 
print() 
print("Sum of the elements is slice1=",sum) 
print("Slice2") 
sum=0 
for a in s2: 
    sum+=a 
    print(a,'',end='') 
print() 
avg=sum/len(s2) 
print("Sum of the elements is slice2=",sum) 
print("Sum of the elements is slice2=",avg) 
