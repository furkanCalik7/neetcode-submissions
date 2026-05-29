class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subset_count = 2 ** len(nums)

        for i in range(subset_count):
            subset = []
            for j in range(len(nums)):
                if i & (1 << j):
                    subset.append(nums[j])
                
            subsets.append(subset)

        return subsets
