class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i, j= 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
            # print(nums[i], val, i, j)
        return j

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
    print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
    print(solution.removeElement([2], 3))