class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // char arr
        // A - Z (26)
        // Task CPU needs to process
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task] += 1;
        }

        priority_queue<int> maxHeap;
        for (auto [c , cnt] : count) {
            maxHeap.push(cnt);
        }

        int time = 0;
        queue<pair<int, int>> q;
        while (!maxHeap.empty() || !q.empty()) {
            time++;

            if (maxHeap.empty()) {
                time = q.front().second;
            } else {
                int cnt = maxHeap.top() - 1;
                maxHeap.pop();
                if (cnt > 0) {
                    q.push({cnt, time + n});
                }
            }

            if (!q.empty() && q.front().second == time) {
                maxHeap.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};
