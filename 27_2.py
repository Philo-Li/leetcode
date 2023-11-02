class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slowIndex, quickIndex = 0, 0
        while quickIndex < len(nums):
            # print('slowIndex', slowIndex, 'quickIndex', quickIndex, nums[slowIndex], nums[quickIndex])
            if nums[quickIndex] == val:
                # move quickIndex item to slowIndex
                nums[slowIndex] = nums[quickIndex]
                quickIndex += 1
            else:
                slowIndex += 1
                quickIndex += 1
        
        return slowIndex
            

        

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement(nums = [3, 2, 2, 3], val = 3))
    print(solution.removeElement(nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2))