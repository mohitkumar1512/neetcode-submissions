class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int,int>> pq;
        for (int i = 0; i< points.size(); i++){
            pq.push({euclideanDistance(points[i]), i});
            if (pq.size() > k){
                pq.pop();
            }
        }

        vector<vector<int>> res;
        while (!pq.empty()){
            res.push_back(points[pq.top().second]);
            pq.pop();
        }
        return res;
    }
    int euclideanDistance(vector<int>& point){
        return point[0]*point[0] + point[1]*point[1];
    }
};
