class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        mod = (10 ** 9) + 7
        B = [1] * n

        mul = 1
        for i in range(n):
            B[i] = mul % mod
            nextVal = mul * A[i]
            mul = nextVal % mod

        mul = 1
        for i in range(n - 1, -1, -1):
            B[i] = (B[i] * mul) % mod
            nextVal = mul * A[i]
            mul = nextVal % mod

        return B

ans = Solution()
arr = [1, 2, 3, 4]
print(ans.solve(arr))