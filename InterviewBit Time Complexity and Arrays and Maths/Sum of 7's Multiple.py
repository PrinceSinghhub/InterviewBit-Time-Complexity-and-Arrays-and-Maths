class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        n1 = A // 7
        if A % 7 != 0:
            n1 = n1 + 1
        n2 = B // 7
        return 7 * (((n2 - n1 + 1) * (n2 + n1)) // 2)

ans = Solution()
print(ans.solve(1054,564))