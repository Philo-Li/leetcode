class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right :
            middle = left + (right - left) // 2

            if nums[middle] > target :
                right = middle - 1
            elif (nums[middle] < target):
                left = middle + 1
            else:
                return middle
        return -1

    def search2(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))
    print(solution.search([-1,0,3,5,9,12], 2))
    print(solution.search2([-1,0,3,5,9,12], 9))
    print(solution.search2([-1,0,3,5,9,12], 2))