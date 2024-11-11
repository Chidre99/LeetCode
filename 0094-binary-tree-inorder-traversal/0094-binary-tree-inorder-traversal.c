/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void inorderHelper(struct TreeNode* root, int* result, int* returnSize) {
    if (root != NULL) {
        inorderHelper(root->left, result, returnSize);
        result[(*returnSize)++] = root->val; // Store the value in the result array and increment returnSize
        inorderHelper(root->right, result, returnSize);
    }
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    int* result = (int*)malloc(100 * sizeof(int)); // Allocate memory for result array
    
    // Call the helper function to fill the result array
    inorderHelper(root, result, returnSize);
    
    return result; // Return the result array
}