class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        for (auto& interval : intervals) {
            // case 1: current interval ends before new one starts
            if (interval[1] < newInterval[0]) {
                res.push_back(interval);
            }
            // case 2: current interval starts after new one ends
            else if (interval[0] > newInterval[1]) {
                res.push_back(newInterval);
                newInterval = interval; // shift newInterval forward
            }
            // case 3: overlap -- expand newInterval
            else {
                newInterval[0] = min(newInterval[0], interval[0]);
                newInterval[1] = max(newInterval[1], interval[1]);
            }
        }

        res.push_back(newInterval); // always push the final merged interval
        return res;
    }
};
