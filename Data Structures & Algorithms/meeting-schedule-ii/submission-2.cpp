/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<int> start;
        vector<int> end;
        for (auto [s, e] : intervals){
            start.push_back(s);
            end.push_back(e);
        }
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        int res = 0, count = 0, s = 0, e = 0;
        while (s < intervals.size()){
            if (start[s] < end[e]){
                s += 1;
                count += 1;
            } else {
                e += 1;
                count -= 1;
            }
            res = max(res, count);
        }
        return res;
    }
};
