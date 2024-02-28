def find_prime_factors(n):
    factors = [0, 0, 0, 0, 0]
    primes = [2, 3, 5, 7, 11]
    
    for i, prime in enumerate(primes):
        while n % prime == 0:
            factors[i] += 1
            n //= prime
    return factors


T = int(input())
for t in range(1, T+1):
    N = int(input())
    factors = find_prime_factors(N)
    print(f"#{t}", ' '.join(map(str, factors)))