lst1,lst2=[],[]
while True:
    try:
        s=str(input())
        if s=="pop":
            if lst1:
                lst1.pop()
                if lst2:
                    lst2.pop()
        elif s=="min":
            if lst2:
                print(lst2[-1])
        else:
            h=int(s[4:])
            lst1.append(h)
            if not lst2:
                lst2.append(h)
            else:
                lst2.append(min(lst2[-1],h))
    except EOFError:
        break