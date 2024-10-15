int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int minimumDifference(int* nums, int numsSize, int k) {
    if (k < 2) {
        return 0;
    }

    // Step 1: Sort the array
    qsort(nums, numsSize, sizeof(int), compare); // Using quicksort or any sorting algorithm

    // Step 2: Initialize minDifference to a large value
    int minDifference = INT_MAX;

    // Step 3: Sliding window to find minimum difference
    for (int i = 0; i <= numsSize - k; i++) {
        int diff = nums[i + k - 1] - nums[i];  // Difference between the highest and lowest in the window
        if (diff < minDifference) {
            minDifference = diff;
        }
    }

    return minDifference;
}
