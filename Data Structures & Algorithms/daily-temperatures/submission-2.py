class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        stack.append((temperatures[0], 0))

        for i, val in enumerate(temperatures[1:]):
            while len(stack) > 0 and val > stack[-1][0]:
                _, index = stack.pop()
                res[index] = i + 1 - index
            stack.append((val, i + 1))
        
        print(stack)

        while len(stack) > 0:     
            _,i = stack.pop()
            res[i] = 0
        
        return res




