class Solution:

    def delimiter(self, count: int) -> str:
        return f'{count}#'

    # ['Hello', 'Good', 'World'] -> "Hello#4Good#5World"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + self.delimiter(len(s)) + s
        print('ENCODE: ' + res)
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
        
            forward = int(s[i:j])
            res.append(s[j + 1: j + forward + 1])
            i = j + forward + 1

        return res



