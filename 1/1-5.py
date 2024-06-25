s=str(input())
maxi=0
nlo,plo=[],[]
for i in range(len(s)):
    if s[i]=="n":
        nlo.append(i)
    if s[i]=="+":
        plo.append(i)
if len(nlo)>2:    
    if s[:nlo[0]]!="0":
        maxi=max(maxi,int(s[nlo[0]+2:plo[0]]))
    if s[plo[-1]+1:nlo[-1]]!="0":
        maxi=max(maxi,int(s[nlo[-1]+2:]))
    for j in range(len(nlo)-2):
        if s[plo[j]+1:nlo[j+1]]!="0":
            maxi=max(maxi,int(s[nlo[j+1]+2:plo[j+1]]))
if len(nlo)==1 and s[:nlo[0]]!="0":
    maxi=int(s[nlo[0]+2:])
if len(nlo)==2:
    if s[:nlo[0]]=="0":
        maxi=int(s[nlo[1]+2:])
    if s[plo[0]+1:nlo[1]]=="0":
        maxi=int(s[nlo[0]+2:plo[0]])
    else:
        maxi=max(int(s[nlo[1]+2:]),int(s[nlo[0]+2:plo[0]]))
print(f"n^{maxi}")