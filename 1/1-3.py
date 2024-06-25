s=str(input())
s=s.lower()
lets=["a","e","i","o","u","y"]
out=[""]
for i in s:
    if i not in lets:
        out.append(i)
print(".".join(out))