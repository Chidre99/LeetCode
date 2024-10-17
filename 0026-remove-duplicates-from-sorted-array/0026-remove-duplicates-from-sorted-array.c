int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0; // If the array is empty, return 0.
    }

    // Initialize a pointer for the position of the unique elements.
    int uniqueIndex = 0;

    // Traverse through the array.
    for (int i = 1; i < numsSize; i++) {
        // If we find a new unique element, move it to the position after the last unique element.
        if (nums[i] != nums[uniqueIndex]) {
            uniqueIndex++;
            nums[uniqueIndex] = nums[i];
        }
    }

    // Return the length of the array with unique elements.
    return uniqueIndex + 1;
}
