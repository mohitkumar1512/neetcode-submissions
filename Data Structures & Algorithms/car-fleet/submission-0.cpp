class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> cars(n);
        
        for (int i = 0; i < n; i++)
            cars[i] = {position[i], speed[i]};
        
        // Sort descending by position (closest to target first)
        sort(cars.begin(), cars.end(), greater<pair<int,int>>());
        
        stack<double> st;
        for (auto& [pos, spd] : cars) {
            double time = (double)(target - pos) / spd;
            // Only push if this car is slower than the fleet ahead
            if (st.empty() || time > st.top())
                st.push(time);
            // else: it catches up → same fleet, discard
        }
        
        return st.size();
    
    }
};
