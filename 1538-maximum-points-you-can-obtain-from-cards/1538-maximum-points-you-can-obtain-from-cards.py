class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_score = curr_sum = sum(cardPoints[:k])

        for i in range(1, k + 1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
            max_score = max(max_score, curr_sum)

        return max_score