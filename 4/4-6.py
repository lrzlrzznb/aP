def merge_sort(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = len(lst) // 2
    left, inv_left = merge_sort(lst[:middle])
    right, inv_right = merge_sort(lst[middle:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge
def merge(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return merged, inv_count
while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    _, inversions = merge_sort(lst)
    print(inversions)

