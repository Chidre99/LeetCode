/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int closestValue(struct TreeNode* root, double target) {
    int closestNode = root->val; // Initialize with the root value
    while (root != NULL) {
        // Update closestNode if:
        // 1. The current node is closer to the target, OR
        // 2. The difference is the same, but the current node's value is smaller.
        if (fabs(root->val - target) < fabs(closestNode - target) || 
            (fabs(root->val - target) == fabs(closestNode - target) && root->val < closestNode)) {
            closestNode = root->val;
        }
        
        // Move to the appropriate subtree
        if (target < root->val) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return closestNode;
}
