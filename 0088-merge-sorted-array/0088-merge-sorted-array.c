void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int j = 0;  // Pointer for nums2

    // Step 1: Fill nums1 with elements from nums2
    for (int i = 0; i < nums1Size && j < nums2Size; i++) {
        if (nums1[i] == 0) {
            nums1[i] = nums2[j];
            j++;
        }
    }

    // Step 2: Sort the merged array manually using Bubble Sort
    bubbleSort(nums1, nums1Size);
}

void bubbleSort(int* arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
