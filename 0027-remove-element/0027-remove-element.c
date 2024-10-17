int removeElement(int* nums, int numsSize, int val) {
    int k = 0;  // Pointer for the next position to place a non-val element
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[k] = nums[i];  // Place the non-val element in the next position
            k++;
        }
    }
    
    return k;  // k is the new size of the array without val elements
}
