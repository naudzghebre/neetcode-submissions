class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == '+':
                r, l = stack.pop(), stack.pop()
                s = str( int(l) + int(r) )
                stack.extend([l, r, s])
            elif o == 'D':
                stack.append(str(2 * int(stack[-1])))
            elif o == 'C':
                stack.pop()
            else:
                stack.append(o)
        
        s = 0
        for o in stack:
            s += int(o)
        return s