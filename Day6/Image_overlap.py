class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a_1=[]
        b_1=[]
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]==1:
                    a_1.append((i,j))
                if B[i][j]==1:
                    b_1.append((i,j))
        
        d={}
        ans=0
        
        for a_x,a_y in a_1:
            for b_x,b_y in b_1:
                translation = (b_x-a_x, b_y-a_y)
                if translation in d:
                    d[translation] += 1
                else:
                    d[translation] = 1
                ans=max(ans,d[translation])
        return ans
