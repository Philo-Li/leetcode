class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        last, finder = 0, 0
        for last in range(len(nums) - 1):
            while nums[last] == nums[finder]:
                finder += 1
                if finder == len(nums):
                    return last + 1
            # print(last, finder, nums[last], nums[finder])
            nums[last+1] = nums[finder]
            last += 1
        return last + 1

if __name__ == '__main__':
    solution = Solution()
    # print(solution.removeDuplicates([1,1,2]))
    print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
