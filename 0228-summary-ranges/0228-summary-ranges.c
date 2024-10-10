/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char* createRangeString(int start, int end) {
    char* range = (char*)malloc(25 * sizeof(char)); // Allocate memory for the range string
    if (start == end) {
        sprintf(range, "%d", start); // Single number, no range
    } else {
        sprintf(range, "%d->%d", start, end); // Range from start to end
    }
    return range;
}

char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    // Allocate memory for the output array
    char** result = (char**)malloc(numsSize * sizeof(char*));
    int start = 0, end = 0, idx = 0;

    for (int i = 1; i <= numsSize; i++) {
        // If the current number is not contiguous or we reached the end of the array
        if (i == numsSize || nums[i] != nums[i - 1] + 1) {
            end = i - 1;
            // Create a range string for the current range and store it
            result[idx++] = createRangeString(nums[start], nums[end]);
            start = i; // Start new range
        }
    }

    *returnSize = idx; // Set the return size
    return result;
}