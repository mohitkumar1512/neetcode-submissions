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
int maxDiam = 0;

    int height(TreeNode* node) {
        if (!node) return 0;

        int left  = height(node->left);
        int right = height(node->right);

        maxDiam = max(maxDiam, left + right);  // diameter through this node

        return 1 + max(left, right);           // height of this subtree
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return maxDiam;
    }
};
