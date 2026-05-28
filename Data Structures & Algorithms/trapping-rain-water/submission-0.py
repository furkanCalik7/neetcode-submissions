class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        min_height = min(height[i], height[j])
        trapped = 0

        while i < j:
            if height[i] < height[j]:
                i+=1
                trapped += max(min_height - height[i], 0)
                if height[i] > min_height:
                    min_height = min(height[i], height[j])
            else: 
                j-=1 
                trapped += max(min_height - height[j], 0)
                if height[j] > min_height:
                    min_height = min(height[i], height[j])
             
        return trapped




