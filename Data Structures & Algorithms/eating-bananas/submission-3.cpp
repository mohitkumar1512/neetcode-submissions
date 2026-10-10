class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1; 
        int right = INT_MIN; 
        for (auto pile : piles){
            right = max(right, pile);
        }
        int minSpeed = INT_MAX;
        while (left <= right){
            int mid = left + (right - left) / 2;
            int duration = 0;
            for (int& pile : piles){
                duration += ((pile + mid - 1) / mid);
            }
            if (duration <= h) {minSpeed = min(minSpeed, mid); right = mid - 1;}
            else left = mid + 1;
        }
        return minSpeed;
    }
};
