class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DFS
        def generate_subsets(nums, k, start, c, res):
            if len(c) == k:
                res.append(c[:])
                return
            for i in range(start, len(nums) - (k - len(c)) + 1):
                c.append(nums[i])
                generate_subsets(nums, k, i + 1, c, res)
                c.pop()

        res = []
        for k in range(len(nums) + 1):
            generate_subsets(nums, k, 0, [], res)

        return res
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1,2,3]))