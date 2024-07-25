# Python solution file
num= input()
lis=list(map(int,input().split()))
cond1=True
for i in range(len(lis)):
    if lis[i]<0:
        cond1=False
for k in range(len(lis)):
    st=f"{lis[k]}"
    if st==st[::-1]:
        cond2=True
        break
    else:
        cond2=False
         
                    
if(cond1 and cond2):
    print("True")
else:
    print("False")            