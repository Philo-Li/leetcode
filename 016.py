class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = 10001
        totalSum = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                distance = target - total
                # print(i, left, right, total, 'distance', distance, 'closest', closest, 'hey')
                if closest > abs(distance):
                    closest = abs(distance)
                    totalSum = total
                if distance == 0:
                    return totalSum
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return totalSum

if __name__ == '__main__':
    solution = Solution()
    # print(solution.threeSumClosest([-1,2,1,-4], 1))
    # print(solution.threeSumClosest([1, 1, 1, 1], 0))
    # print(solution.threeSumClosest([1,1,1,0], -100))
    # print(solution.threeSumClosest([0,1,2], 3))
    print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))