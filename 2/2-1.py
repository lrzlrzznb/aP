a,b,c,d=map(int,input().split())
for i in range(min(b,d),0,-1):
    if b%i==0 and d%i==0:
        m=b*d//i
        break
a*=m//b
c*=m//d
e=a+c
for i in range(min(e,m),0,-1):
    if e%i==0 and m%i==0:
        e//=i
        m//=i
print(f"{e}/{m}")