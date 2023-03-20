class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            print(k, i, nums[k], nums[i])
        return k

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1,1,2]))
    # print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
