class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        for (int i = 0; i <= n; i++){
            res.push_back(countBit(i));
        }
        return res;
    }
    int countBit(int n) {
        int res = 0;
        while (n){
            n &= (n-1);
            res += 1;
        }
        return res;
    }
};
