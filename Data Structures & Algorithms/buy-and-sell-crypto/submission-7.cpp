class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1;
        int maxy = 0;
        while (r < prices.size()){
            maxy = max(prices[r] - prices[l], maxy);
            if (prices[r] < prices[l]){
                l = r;
            }
            r += 1;

        }
        return maxy;
    }
};
