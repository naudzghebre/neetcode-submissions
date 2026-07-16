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
        res = []
        ind = 0
        while ind < len(s):
            j = ind
            while s[j] != '#':
                j += 1
        
            forward = int(s[ind:j])
            res.append(s[j + 1: j + forward + 1])
            ind = j + forward + 1
        print(res)

        return res



