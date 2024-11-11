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
 void preorderHelper(struct TreeNode* root, int* result, int* returnSize) {
    if (root != NULL) {
        result[(*returnSize)++] = root->val;
        preorderHelper(root->left, result, returnSize); 
        preorderHelper(root->right, result, returnSize);
    }
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    int* result = (int*)malloc(100 * sizeof(int)); // Allocate memory for result array
    
    // Call the helper function to fill the result array
    preorderHelper(root, result, returnSize);
    
    return result; // Return the result array
}