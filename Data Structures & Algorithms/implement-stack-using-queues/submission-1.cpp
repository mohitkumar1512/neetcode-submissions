class MyStack {
public:
    queue<int> stack1;
    queue<int> stack2;
    MyStack() {
    }
    
    void push(int x) {
        this->stack2.push(x);
        while (!this->stack1.empty()){
            this->stack2.push(this->stack1.front());
            this->stack1.pop();
        }
        this->stack1 = this->stack2;
        this->stack2 = queue<int>();
    }
    
    int pop() {
        int res = stack1.front();
        stack1.pop();
        return res;
    }
    
    int top() {
        return stack1.front();
    }
    
    bool empty() {
        return stack1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */