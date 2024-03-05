import math
def getMyDivisor(n):
    
    divisorsList = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisorsList.append(i)
            if (i**2) != n:
                divisorsList.append(n // i)