class Solution {
    int dfs(TreeNode* node) {
        if (!node) return 0;

        int left  = dfs(node->left);
        int right = dfs(node->right);

        if (left == -1 || right == -1)       return -1;  // propagate failure
        if (abs(left - right) > 1)           return -1;  // unbalanced here

        return 1 + max(left, right);
    }

public:
    bool isBalanced(TreeNode* root) {
        return dfs(root) != -1;
    }
};