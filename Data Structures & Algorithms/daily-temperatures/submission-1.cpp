class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> s;
        vector<int> output(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++){
            while (!s.empty() && s.top().first < temperatures[i]){
                auto [val, index] = s.top(); s.pop();
                output[index] = i - index;
            }
            s.push({temperatures[i], i});
        }
        return output;
    }
};
