class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++)
            dp[i] = dp[i >> 1] + (i & 1);
        return dp;
    //     vector<int> res;
    //     for (int i = 0; i <= n; i++){
    //         res.push_back(countBit(i));
    //     }
    //     return res;
    // }
    // int countBit(int n) {
    //     int res = 0;
    //     while (n){
    //         n &= (n-1);
    //         res += 1;
    //     }
    //     return res;
    }
};
