class Solution(object):
    def mergeAltenately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

if __name__ == '__main__':
    solution = Solution()
    # print(solution.mergeAltenately(word1 = "abc", word2 = "pqr"))
    print(solution.mergeAltenately(word1 = "ab", word2 = "pqrs"))