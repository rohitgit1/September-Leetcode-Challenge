class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {char:index for index, char in enumerate(S)}
        l = 0
        r = 0
        res = []
        
        for index,char in enumerate(S):
            r = max(r,d[char])
            if index == r:
                res.append(r-l+1)
                l = index+1
        return res
