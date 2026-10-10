/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    unordered_map<Node*, Node*> visited;
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;

        // if already cloned, return the existing clone (avoid infinite loop)
        if (visited.count(node)) return visited[node];

        // create clone and register it BEFORE recursing into neighbors
        Node* newNode = new Node(node->val);
        visited[node] = newNode;

        // now clone all neighbors
        for (auto neighbor : node->neighbors) {
            newNode->neighbors.push_back(cloneGraph(neighbor));
        }

        return newNode;

    }
};
