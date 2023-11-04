class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer: l, r
        # 1. two for loop, and length will be len(nums)
        # 2. slip window, only use one for loop
        # the key with slip window is the left pointer will continuously adjust according to the sum of the subarray
        # so the time time complexity will reduced from O(n^2) to O(n)
        min_len = float('inf')
        for l in range(len(nums)):
            s = 0
            for r in range(l, len(nums)):
                s += nums[r]
                if s >= target:
                    min_len = min(min_len, r - l + 1)
                    break
        return min_len if min_len != float('inf') else 0

    def minSubArrayLen2(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # slippery window
        



if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(4, [1, 4, 4]))
    print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))