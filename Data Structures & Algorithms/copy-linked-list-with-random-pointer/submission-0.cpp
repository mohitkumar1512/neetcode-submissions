class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        unordered_map<Node*, Node*> mp; // old -> new

        // First pass: create all new nodes
        Node* curr = head;
        while (curr) {
            mp[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Second pass: assign next and random
        curr = head;
        while (curr) {
            if (curr->next)   mp[curr]->next   = mp[curr->next];
            if (curr->random) mp[curr]->random = mp[curr->random];
            curr = curr->next;
        }

        return mp[head];
    }
};