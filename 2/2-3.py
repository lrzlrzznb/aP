cases = int(input())
for i in range(cases):    
    situation = "alive"
    n,m, b= map(int, input().split())
    a={}
    for i in range(n):
        x,y = map(int,input().split())
        if x not in a:
            a[x] = [y]
        else:
            a[x].append(y)
        
    c = sorted(a)
    for i in c:
        if m >= len(a[i]):
            b -= sum(a[i])
        else:
            a[i] = sorted(a[i], reverse=True)
            b -= sum(a[i][:m])
        if b <= 0:
            situation = i
            break
    print(situation)
