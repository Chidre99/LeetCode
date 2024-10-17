/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Create a map to store the numbers we've seen and their indices
    int* result = (int*)malloc(2 * sizeof(int)); // We will return two indices
    *returnSize = 0;  // Initialize return size to 0
    
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;  // We're returning two indices
                return result;
            }
        }
    }
    return result; // In case no solution is found
}
