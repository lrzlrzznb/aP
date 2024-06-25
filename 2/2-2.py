n,w=map(int,input().split())
candies=[]
for i in range(n):
    p,q=map(int,input().split())
    for i in range(q):
        candies.append(p/q)
candies.sort(reverse=True)
value=sum(candies[:w])
print("{:.1f}".format(value))
