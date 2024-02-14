a = int(input())
b = int(input())
c = int(input()) 

result = list(str(a * b * c)) ## 35615

for i in range(10):
    print(result.count(str(i)))