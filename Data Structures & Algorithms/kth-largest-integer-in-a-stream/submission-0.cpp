class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> pq;
    int kV;
    KthLargest(int k, vector<int>& nums) {
        kV = k;
        for (int num : nums){
            pq.push(num);
            if(pq.size() > k){
                pq.pop();
            }
        }
    }
    
    int add(int val) {
        pq.push(val);
        while(pq.size() > kV){
            pq.pop();
        }
        return pq.top();
    }
};
