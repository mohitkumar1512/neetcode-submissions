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
        bool isValidBST(TreeNode* root) {
        if (!root) return true;
        return BST(root, LONG_MIN, LONG_MAX);
    }

    bool BST(TreeNode* root, long min, long max) {
        if (!root) return true;
        
        if (root->left) {
            if (root->left->val >= root->val || root->left->val <= min) return false;
        }
        if (root->right) {
            if (root->right->val <= root->val || root->right->val >= max) return false;
        }
        
        return BST(root->left, min, root->val) && BST(root->right, root->val, max);
    }
};
