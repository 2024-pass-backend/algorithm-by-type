#include <iostream>
#include <vector>

struct Count {
    int zero;
    int one;
};

Count fibonacci(int n, std::vector<Count> &memo) {
    if (memo[n].zero != -1 && memo[n].one != -1) {
        return memo[n];
    }
    if (n == 0) {
        memo[n] = {1, 0};
        return memo[n];
    } else if (n == 1) {
        memo[n] = {0, 1};
        return memo[n];
    } else {
        Count c1 = fibonacci(n - 1, memo);
        Count c2 = fibonacci(n - 2, memo);
        memo[n] = {c1.zero + c2.zero, c1.one + c2.one};
        return memo[n];
    }
}

int main() {
    int T, N;
    std::cin >> T;

    std::vector<Count> memo(41, {-1, -1}); 

    for (int i = 0; i < T; i++) {
        std::cin >> N;
        Count result = fibonacci(N, memo);
        std::cout << result.zero << " " << result.one << std::endl;
    }

    return 0;
}
