/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    // Sort the array first
    qsort(nums, numsSize, sizeof(int), compare);
    
    // Allocate memory for the return array
    int** result = (int**)malloc(sizeof(int*) * 1000);  // Adjust size as needed
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(sizeof(int) * 1000);
    
    // Loop for the first element
    for (int i = 0; i < numsSize - 3; i++) {
        // Skip duplicate elements
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        // Loop for the second element
        for (int j = i + 1; j < numsSize - 2; j++) {
            // Skip duplicate elements
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;
            
            // Two-pointer approach for the remaining two elements
            int left = j + 1;
            int right = numsSize - 1;
            
            while (left < right) {
                long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                
                if (sum == target) {
                    // Allocate memory for one result
                    result[*returnSize] = (int*)malloc(sizeof(int) * 4);
                    result[*returnSize][0] = nums[i];
                    result[*returnSize][1] = nums[j];
                    result[*returnSize][2] = nums[left];
                    result[*returnSize][3] = nums[right];
                    
                    // Set the column size to 4
                    (*returnColumnSizes)[*returnSize] = 4;
                    (*returnSize)++;
                    
                    // Move the pointers and avoid duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }
    
    // Reallocate memory to fit the exact number of results
    result = (int**)realloc(result, sizeof(int*) * (*returnSize));
    *returnColumnSizes = (int*)realloc(*returnColumnSizes, sizeof(int) * (*returnSize));
    
    return result;
}
