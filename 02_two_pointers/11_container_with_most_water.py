class Solution:
    def maxArea(self, height: list[int]) -> int:
        i,j=0,len(height)-1
        m=0
        while i<j:
            h=min(height[i],height[j]) * (j-i)
            m=max(m,h)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return m
