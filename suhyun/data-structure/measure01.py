import math
def divisor(number):
    result = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            result.append(i)
            if i < number // i:
                result.append(number // i)
    result.sort()
    return result

arr = divisor(16)
print(arr)