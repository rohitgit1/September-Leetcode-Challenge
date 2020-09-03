class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep=''
        len_s=len(s)
        for i in range(len_s//2):
            rep=rep+s[i]
            if (len_s % len(rep)==0):
                if rep*(len_s//len(rep))==s:
                    return True
        return False
        
        
