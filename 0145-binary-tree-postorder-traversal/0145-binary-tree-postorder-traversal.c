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
void postrorderHelper(struct TreeNode* root, int* result, int* returnSize) {
    if (root != NULL) {
        postrorderHelper(root->left, result, returnSize); 
        postrorderHelper(root->right, result, returnSize);
        result[(*returnSize)++] = root->val;
    }
}

int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    int* result = (int*)malloc(100 * sizeof(int)); // Allocate memory for result array
    
    // Call the helper function to fill the result array
    postrorderHelper(root, result, returnSize);
    
    return result; // Return the result array
}