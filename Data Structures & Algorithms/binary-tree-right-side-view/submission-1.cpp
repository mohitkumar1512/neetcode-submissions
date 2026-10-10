/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (root){
            queue<TreeNode*> q;
            q.push(root);
            while(!q.empty()){
                int levelS = q.size();

                for (int i = 0; i < levelS; i++){
                    TreeNode* node = q.front(); q.pop();
                    if (i == levelS - 1){
                        res.push_back(node->val);
                    }
                    if (node->left) q.push(node->left);
                    if (node->right) q.push(node->right);
                }
            }
        }
        return res;
    }
};
