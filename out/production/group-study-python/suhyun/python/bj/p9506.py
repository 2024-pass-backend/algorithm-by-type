while True:
    n = int(input())
    if n == -1:
        break
    
    arr = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            sum += i
    if sum == n:
        print(str(n) + " = ", end='')
        for i in range(len(arr) - 1):
            print(str(arr[i]) + " + ", end='')
        print(arr[len(arr) - 1])
    else:
        print(str(n) + " is NOT perfect.")
    
        