answer = []
def Queen(s):
    for col in range(1, 9):
        for j in range(len(s)):
            if (str(col) == s[j] or
                    abs(col - int(s[j])) == abs(len(s) - j)): 
                break
        else:
            if len(s) == 7:
                answer.append(s + str(col))
            else:
                Queen(s + str(col))
Queen('')
n = int(input())
for _ in range(n):
    a = int(input())
    print(answer[a - 1])
