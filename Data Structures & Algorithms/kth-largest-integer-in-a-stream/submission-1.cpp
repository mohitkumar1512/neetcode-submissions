class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int kV;
    KthLargest(int k, vector<int>& nums) {
        kV = k;
        for (int num : nums){
            add(num);
        }
    }
    
    int add(int val) {
        pq.push(val);
        if(pq.size() > kV){
            pq.pop();
        }
        return pq.top();
    }
};
