t=int(input())
for i in range(t):
    lst=[]
    n=int(input())
    for j in range(n):
        tp,x=map(int,input().split())
        if tp==1:
            lst.append(x)
        if tp==2:
            if x==0:
                del lst[0]
            if x==1:
                del lst[-1]
    if len(lst)==0:
        print("NULL")
    else:
        print(" ".join(map(str,lst)))