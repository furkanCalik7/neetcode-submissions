class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        subset = []


        def dfs(i):
            if i == n:
                subsets.append(subset[:]) 
                return
            ## without current element
            dfs(i + 1)
            
            ## with current element
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

        dfs(0)

        return subsets
