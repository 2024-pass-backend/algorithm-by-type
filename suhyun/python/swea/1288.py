# n이 2라고 가정, 첫번째는 2, 4, ... 2k
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [0] * 10
    cnt, num = 0, 1
    val = 1
    while True:
        if arr[0] != 0 and arr[1] != 0 and arr[2] != 0 and arr[3] != 0 and arr[4] != 0 and arr[5] != 0 and arr[6] != 0 and arr[7] != 0 and arr[8] != 0 and arr[9] != 0:
            break
        val = n * num
        n_chars = str(val)
        for elem in n_chars:
            # print("n_chars = " + n_chars + " / " + str(int(elem)) + "출력확인")
            arr[int(elem)] = 1
        num += 1
    print(f'#{tc} {val}')