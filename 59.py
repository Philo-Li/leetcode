class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0 # start point, startx: row index, starty: column index
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop + 1): # for every loop, offset plus 1. offset starts with 1
            for i in range(starty, n - offset): # from left to right, [ )
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset): # from up to down
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1): # from right to left
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1): # from dowm to up
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        
        if n %2 != 0: # if n is odd, fill the mid
            nums[mid][mid] = count
        return nums



if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(3))
    print(solution.generateMatrix(1))