/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root) {
    if(root != NULL){
        int x;
        x = 1 + countNodes(root->left) + countNodes(root->right);
        return x ;
    }
        return 0;
}