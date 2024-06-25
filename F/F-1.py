def dfs(node,level):
    if ans[level]==0:
        ans[level]=node
    for next in tree[node][::-1]:
        if next!=-1:
            dfs(next,level+1)
n=int(input())
tree={}
ans=[0]*n
for i in range(n):
    tree[i+1]=list(map(int,input().split()))
dfs(1,0)
res=[]
for i in ans:
    if i: res.append(i)
    else: break
print(*res)