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
    bool isBalanced(TreeNode* root) {
        return dfs(root)[0] == 1; //checks if the whole tree (rooted at root) is balanced.
    }

//This recursive function computes two things for every subtree:
// - Whether it’s balanced (1 for balanced, 0 for not balnced)
// - Its height
// Returns them as a vector {balanced, height}.
    vector<int> dfs(TreeNode* root) {
        if(!root){
            return{1, 0}; //empty subtree is balanced
        }

        vector<int> left = dfs(root->left);
        vector<int> right = dfs(root->right);

        bool balanced = (left[0] == 1 && right[0] == 1) && (abs(left[1] - right[1]) <= 1);
        int height = 1 + max(left[1], right[1]);

        return {balanced ? 1 : 0, height};
    }
};
