class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int res = 0;
        int end = intervals[0][1];
        int curr_start = -1;
        int curr_end = -1;

        for (int i = 1; i < intervals.size(); i++){
            curr_start = intervals[i][0];
            curr_end = intervals[i][1];
            if (end > curr_start){
                res += 1;
                end = min(end, curr_end);
                
            } else {
                end = curr_end;
            }
        }
        return res;
        
    }
};
