n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
if k==0:
    print(nums[0]-1 if nums[0]>1 else -1)
else:
    if k<n and nums[k-1]==nums[k]:
        print(-1)
    else:
        print(nums[k-1])