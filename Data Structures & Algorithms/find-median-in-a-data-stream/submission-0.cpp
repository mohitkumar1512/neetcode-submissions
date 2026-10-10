class MedianFinder {
public:
    priority_queue<int, vector<int>, greater<int>> large;
    priority_queue<int, vector<int>, less<int>> small;
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        small.push(num);

        if (small.size() > large.size() + 1){
            large.push(small.top());
            small.pop();
        }
        if (!large.empty() && small.top() > large.top()) {
            large.push(small.top());
            small.pop();
        }
        if (large.size() > small.size() + 1) {
            small.push(large.top());
            large.pop();
        }
    }
    
    double findMedian() {
        if (small.size() == large.size()) {
            return (large.top() + small.top()) / 2.0;
        } 
        return large.size() > small.size() ? large.top() : small.top();
        
    }
};
