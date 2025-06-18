class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = skill[0] + skill[-1]
        res = 0
        left, right = 0, len(skill) - 1
        while left < right:
            if skill[left] + skill[right] != total:
                return -1
            res += skill[left] * skill[right]
            left += 1
            right -= 1
        return res
