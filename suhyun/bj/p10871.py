a, x = tuple(map(int, input().split()))
a_list = list(map(int, input().split()))

for elem in a_list:
    if elem < x:
        print(elem, end=' ')

 