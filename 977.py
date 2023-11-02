class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # first square then sort ( O(n + nlog n) )
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums

    def sortedSquares2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # two pointers
        # original array is sorted, so the square will be the first of the array or the last
        # so define a new array named result which is the same size as the original one
        # k point the last of the result array
        l, r, i= 0, len(nums) - 1, len(nums) - 1
        # define a new array
        res = [float('inf')] * len(nums)

        while l <= r:
            if nums[l] ** 2 > nums[r] **2:
                res[i] = nums[l] ** 2
                l += 1 # move left pointer
            else:
                res[i] = nums[r] ** 2
                r -= 1 # move right pointer
            i -= 1 # move result pointer
        return res

    def sortedSquares3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares([-4, -1, -1, 3, 11]))
    print(solution.sortedSquares([-7, -3, 2, 3, 11]))
    print(solution.sortedSquares2([-4, -1, -1, 3, 11]))
    print(solution.sortedSquares2([-7, -3, 2, 3, 11]))
    print(solution.sortedSquares2([-4, -1, -1, 3, 11]))
    print(solution.sortedSquares2([-7, -3, 2, 3, 11]))
