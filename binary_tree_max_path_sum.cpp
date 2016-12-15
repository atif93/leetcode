/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max = 0, lmax, rmax;
        
        if(root == NULL) {
            return 0;
        }
        
        max = root->val;
        
        int rvalue = 0, lvalue = 0;
        if(root->left!= NULL) {
            lmax = maxPathSum(root->left);
            if(max < lmax) {
                max = lmax;
            } 
            if(root->left->val>0) {
                lvalue = root->left->val;   
            }
        }
        if(root->right!= NULL) {
            rmax = maxPathSum(root->right);
            if(max < rmax) {
                max = rmax;
            } 
            if(root->right->val>0) {
                rvalue = root->right->val;   
            }
        }
        if(rvalue + lvalue + root->val > max) {
            max = rvalue + lvalue + root->val;
        }
        if(lvalue > rvalue) {
            root->val = root->val + lvalue;
        } else if(rvalue > lvalue) {
            root->val = root->val + rvalue;
        }
        return max;
    }
};