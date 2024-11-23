/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDiffInBST(struct TreeNode* root) {
    int minDiff = INT_MAX;    // Initialize the minimum difference to a large value
    int prev = -1;            // Initialize `prev` to an invalid value (or NULL equivalent)

    void inOrderTraversal(struct TreeNode* node) {
        if (node == NULL) return;

        // Recur on the left subtree
        inOrderTraversal(node->left);

        // Process the current node
        if (prev != -1) {  // Ensure `prev` is initialized
            int diff = abs(node->val - prev);
            if (diff < minDiff) {
                minDiff = diff;
            }
        }
        prev = node->val;  // Update `prev` to the current node value

        // Recur on the right subtree
        inOrderTraversal(node->right);
    }

    inOrderTraversal(root);  // Start in-order traversal
    return minDiff;
}