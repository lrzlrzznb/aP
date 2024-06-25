n=int(input())
def prime(n0):
    judge=True
    x=int(n0**0.5)
    for i in range(2,x+1):
        if n0%i==0:
            judge=False
    return judge
if n%2==1:
    print("2"+str(n-2))
if n%2==0:
    for i in range(3,n//2+1,2):
        if prime(i)==True and prime(n-i)==True:
            print(str(i)+" "+str(n-i))
            break