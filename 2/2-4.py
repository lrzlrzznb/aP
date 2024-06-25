n=int(input())
lst=list(map(int,input().split()))
record={}
def ess(x):
    isprime=[True]*(x+1)
    for i in range(2,int(x**0.5)+1):
        if isprime[i]:
            for j in range(i**2,x+1,i):
                isprime[j]=False
    return set([t**2 for t in range(2,x+1) if isprime[t]])
lst0=ess(1000000)
for i in lst:
    if i**0.5==int(i**0.5):
        if i in record.keys():
            print(record[i])
        else:
            if i in lst0:
                record[i]="YES"
                print("YES")
            else:
                record[i]="NO"
                print("NO")
    else:
        print("NO")
