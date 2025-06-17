class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_idx = 0
        n = len(spaces)

        for i in range(len(s)):
            if space_idx < n and i == spaces[space_idx]:
                res.append(' ')
                space_idx += 1
            res.append(s[i])
        
        return ''.join(res)
