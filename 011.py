class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxContainer, left, right = 0, 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                maxContainer = max(maxContainer, height[left] * (right - left))
                left += 1
            else:
                maxContainer = max(maxContainer, height[right] * (right - left))
                right -= 1
            
        return maxContainer

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))