L, m = map(int, input().split())
dp = [1]*(L+1)
for i in range(m):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        dp[j] = 0
print(dp.count(1))