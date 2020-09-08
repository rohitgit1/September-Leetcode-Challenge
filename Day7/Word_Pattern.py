class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        c=str.split()
        if len(c)!=len(pattern):
            return False
        
        d={}
        for i in range(len(c)):
            if pattern[i] not in d:
                if c[i] in d.values():
                    return False
                d[pattern[i]]=c[i]
            else:
                if d[pattern[i]]!=c[i]:
                    return False
        return True
            
                
