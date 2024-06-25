s=str(input())
judge=True
stat=0
def dele(s0):
    global judge,s,stat
    if len(s)!=0:
        for i in range(len(s)):
            if s[i]==s0:
                s=s[i+1:len(s)]
                stat=1
                break
        if stat==0:
            judge=False
    else:
        judge=False
    stat=0
dele("h")
dele("e")
dele("l")
dele("l")
dele("o")
if judge==True:
    print("YES")
if judge==False:
    print("NO")
