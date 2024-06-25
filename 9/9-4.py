maxn = 10
sx = [-2,-1,1,2, 2, 1,-1,-2]
sy = [ 1, 2,2,1,-1,-2,-2,-1]
ans = 0
def Dfs(dep: int, x: int, y: int):
    if n*m == dep:
        global ans
        ans += 1
        return
    for r in range(8):
        s = x + sx[r]
        t = y + sy[r]
        if chess[s][t]==False and 0<=s<n and 0<=t<m :
            chess[s][t]=True
            Dfs(dep+1, s, t)
            chess[s][t] = False
for _ in range(int(input())):
    n,m,x,y = map(int, input().split())
    chess = [[False]*maxn for _ in range(maxn)] 
    ans = 0
    chess[x][y] = True
    Dfs(1, x, y)
    print(ans)