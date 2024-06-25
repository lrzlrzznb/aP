nums=list(map(int,input().split()))
nums1=set(nums)
coun={}
maxi=0
output=[]
for i in nums1:
    coun[i]=nums.count(i)
for value in coun.values():
    maxi=max(maxi,value)
for key in coun.keys():
    if coun[key]==maxi:
        output.append(key)
output.sort()
for i in range(len(output)):
    output[i]=str(output[i])
print(" ".join(output))

