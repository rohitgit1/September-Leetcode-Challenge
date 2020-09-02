class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        combination = sorted(list(itertools.permutations(A)),reverse=True)
        
        for x in combination:
            h,i,j,k = x
            hour = ((h*10) + i)
            minute = ((j*10) + k)
            if hour<24 and minute<60:
                return f"{h}{i}:{j}{k}"
        return ''
