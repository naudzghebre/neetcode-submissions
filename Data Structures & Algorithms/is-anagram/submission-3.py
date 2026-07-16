class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t, sdict = list(s), list(t), dict()
        for i in range(len(s)):
            c, d = s[i], t[i]
            if c not in sdict.keys():
                sdict[c] = 0
            if d not in sdict.keys():
                sdict[d] = 0
            sdict[c] += 1
            sdict[d] -= 1
        
        for k in sdict.keys():
            if sdict[k] != 0:
                return False
        return True