class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, 0
        for t in nums:
            if t == 0:
                i += 1
            elif t == 1:
                j += 1
            else:
                k += 1
            # print(t)
        for m in range(len(nums)):
            if m <= i - 1:
                nums[m] = 0
            elif m <= i + j - 1:
                nums[m] = 1
            else:
                nums[m] = 2
        print(nums)
        return nums

if __name__ == '__main__':
    solution = Solution()
    print(solution.sortColors([2,0,2,1,1,0]))