m,n=map(int,input().split())
words=list(map(int,input().split()))
queue=[]
ans=0
for num in words:
    if num not in queue:
        queue.append(num)
        ans+=1
        if len(queue)==m+1:
            queue.pop(0)
print(ans)