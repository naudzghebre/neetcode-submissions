class Solution:
    # O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1
        
        for c in counts:
            if counts[c] != 0:
                return False
        return True
    
    # Return a list with indices representing chars to keep frquency count
    # O(n) - where n is the longest string
    def buildKey(self, s: str) -> str:
        counts = 26 * [0]
        for c in s:
            counts[ord(c) - 97] += 1
        print(counts)
        return ",".join(str(x) for x in counts)

    # O(m * n) where m is number of strings, and n is length of longest string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            k = self.buildKey(s)
            if k not in anagrams:
                anagrams[k] = []
            anagrams[k].append(s)

        groups = []
        for a in anagrams:
            groups.append(anagrams[a])
        return groups
