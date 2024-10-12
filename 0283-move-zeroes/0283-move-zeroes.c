void moveZeroes(int* nums, int numsSize) {
    int zeroIndex = -1;  // To store the index of the first zero
    int nonZeroIndex = -1;  // To store the index of the next non-zero element after a zero

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0 && zeroIndex == -1) {
        // First zero found, store its index
        zeroIndex = i;
        }else if (nums[i] != 0 && zeroIndex != -1) {
        // Non-zero element found after zero
        nonZeroIndex = i;
        
        // Now swap the elements at zeroIndex and nonZeroIndex
        int temp = nums[zeroIndex];
        nums[zeroIndex] = nums[nonZeroIndex];
        nums[nonZeroIndex] = temp;
        
        // Update zeroIndex to look for the next zero
        zeroIndex++;
    }
}

}