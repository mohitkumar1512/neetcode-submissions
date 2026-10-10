class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s;
        
        for(int i = 0; i < operations.size(); i++){
            if(operations[i] == "+"){
                int a = s.top();
                s.pop();
                int b = s.top();
                s.push(a);
                s.push(a + b);
            }
            else if(operations[i] == "C"){
                s.pop();
            }
            else if(operations[i] == "D"){
                s.push(s.top() * 2);
            }
            else{
                s.push(stoi(operations[i]));
            }
        }
        int res = 0;
        while(s.size()){
            int num = s.top();
            s.pop();
            res += num;
            cout << num << endl;
        }
        return res;
    }
};