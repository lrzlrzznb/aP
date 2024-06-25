from collections import deque
t=int(input())
grp={}
for i in range(t):
    grp[i]=list(map(str,input().split()))
queue=deque()
group_queue={i:deque() for i in range(t)}
while True:
    s=list(map(str,input().split()))
    if s==["STOP"]:
        break
    elif s[0]=="ENQUEUE":
        p=s[1]
        for i in range(t):
            if p in grp[i]:
                group_queue[i].append(p)
                if i not in queue:
                    queue.append(i)
                break
    else:
        group=queue[0]
        print(group_queue[group].popleft())
        if not group_queue[group]:
            queue.popleft()
