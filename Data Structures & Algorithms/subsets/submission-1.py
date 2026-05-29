class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []


        def find_subset(subset, index):
            if index == n:
                subsets.append(subset[:]) 
                return

            ## without current element
            find_subset(subset, index + 1)
            
            ## with current element
            subset.append(nums[index])
            find_subset(subset, index + 1)
            subset.pop()

        find_subset([], 0)

        return subsets
