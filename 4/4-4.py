def is_valid_pop_sequence(origin, output):
    if len(origin) != len(output):
        return False  
    stack = []
    bank = list(origin)
    for char in output:
        while (not stack or stack[-1] != char) and bank:
            stack.append(bank.pop(0))
        if not stack or stack[-1] != char:
            return False
        stack.pop() 
    return True
origin = input().strip()
while True:
    try:
        output = input().strip()
        if is_valid_pop_sequence(origin, output):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
