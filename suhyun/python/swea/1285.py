t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_abs = []
    for elem in arr:
        arr_abs.append(abs(elem))
    sorted(arr_abs)
    min_val = min(arr_abs)
    cnt = arr_abs.count(min_val)
    print(f'#{tc} {min_val} {cnt}')