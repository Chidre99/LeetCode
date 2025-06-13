class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
                age = i[-4:-2]
                if int(age) > 60:
                    count = count +1
        return count