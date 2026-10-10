class Solution {
public:
    // unordered_map<int, int> memo;

    int climbStairs(int n) {
        // if (n == 1) return 1;
        // if (n == 2) return 2;
        // if (memo.count(n)) return memo[n];  // already computed
        // return memo[n] = climbStairs(n-1) + climbStairs(n-2);

        if (n == 1) return 1;
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
