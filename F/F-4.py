n, m = map(int, input().split())
expenditure = [int(input()) for _ in range(n)]
left,right = max(expenditure), sum(expenditure)
def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]
            num += 1
        else:
            s += expenditure[i]    
    return [False, True][num > m]
res = 0
def binary_search(lo, hi):
    if lo >= hi:
        global res
        res = lo
        return  
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid + 1
        binary_search(lo, hi)
    else:
        hi = mid
        binary_search(lo, hi)        
binary_search(left, right)
print(res)