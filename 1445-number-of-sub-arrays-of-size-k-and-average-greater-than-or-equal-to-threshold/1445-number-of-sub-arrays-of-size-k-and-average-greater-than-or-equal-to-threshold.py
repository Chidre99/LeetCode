class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = 0
        curent_sum = 0
        count = 0
        size = len(arr)
        while j<size:
            curent_sum += arr[j]
            if j-i+1 == k:
                avg = curent_sum/k
                if avg >= threshold:
                    count = count+1
                curent_sum -= arr[i]
                i+=1
            j+=1
        return count