class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            board[i][j], tmp = "/", board[i][j] # Mark the current cell as visited
            res = dfs(board, word, i + 1, j, k + 1) or \
                  dfs(board, word, i - 1, j, k + 1) or \
                  dfs(board, word, i, j + 1, k + 1) or \
                  dfs(board, word, i, j - 1, k + 1)
            board[i][j] = tmp # Restore the original value after the search
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))