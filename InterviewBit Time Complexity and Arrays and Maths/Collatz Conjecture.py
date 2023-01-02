class Solution:
    # @param A : integer
    # @param B : integer
    # @return an long
    def solve(self, A, B):

        ans = A

        for i in range(B - 1):

            if ans % 2 == 0:
                ans = ans // 2
            else:
                ans = (ans * 3) + 1

        return ans



ans = Solution()
a = 1
b = 3
print(ans.solve(a,b))