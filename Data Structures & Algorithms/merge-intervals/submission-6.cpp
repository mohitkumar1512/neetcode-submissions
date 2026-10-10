class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> res;
        int start = intervals[0][0];
        int end = intervals[0][1];
        int curr_start = -1;
        int curr_end = -1;

        for (int i = 1; i < intervals.size(); i++){
            curr_start = intervals[i][0];
            curr_end = intervals[i][1];
            
            if (end >= curr_start){
                end = max(end, curr_end);
            } else {
                res.push_back({start, end});
                start = curr_start;
                end = curr_end;
            }
        }
        res.push_back({start, end});
        return res;
    }
};
