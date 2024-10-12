int findLengthOfLCIS(int* nums, int numsSize) {
    if(numsSize == 0) return 0;
    int count = 1;
    int maxLength = 1;
    for(int i = 1; i < numsSize; i++){
        if(nums[i-1] < nums[i]){
            count++;
            if(count > maxLength){
                maxLength = count;
            }
        }else if(nums[i-1] >= nums[i]){
            count = 1;
        }
        
    }
    return maxLength;
}