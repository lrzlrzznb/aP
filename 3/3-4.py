n=int(input())
lst=list(map(int,input().split()))
dic={}
nums=[]
t=0
for i in range(n):
    dic[i+1]=lst[i]
lst.sort()
for i in range(n):
    t+=(n-i-1)*lst[i]
    for k,v in dic.items():
        if lst[i]==v:
            nums.append(str(k))
            dic[k]=None
t/=n
print(" ".join(nums))
print("%.2f"%t)
