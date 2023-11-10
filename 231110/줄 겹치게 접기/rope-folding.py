import sys
input = sys.stdin.readline
n, l =  map(int, input().split())
li = [int(input()) for _ in range(n)]
arr1 = []
arr2 = []
result = []
fold_point = 0.5
while fold_point < l:
    for i in range(n):
        if li[i] == fold_point:
            continue
        if li[i] < fold_point:
            diff = fold_point - li[i]
            arr2.append(fold_point+diff)
        else:
            arr1.append(li[i])
    if len(arr2) > len(arr1):
        arr1, arr2 = arr2, arr1
    for x in arr2:
        if x not in arr1:
            break
    else:
        result.append(fold_point)
    fold_point+=0.5
print(len(result))