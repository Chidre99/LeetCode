/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* buildBST(int* nums, int start, int end) {
    if (start > end) return NULL;  // Base case: no elements

    int mid = start + (end - start) / 2;
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = nums[mid];
    node->left = buildBST(nums, start, mid - 1);
    node->right = buildBST(nums, mid + 1, end);

    return node;
}

// Main function to convert sorted array to BST
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    if (numsSize == 0) return NULL;
    return buildBST(nums, 0, numsSize - 1);
}