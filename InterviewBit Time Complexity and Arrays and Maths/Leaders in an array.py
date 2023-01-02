class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        n = len(A)

        Max = [A[n - 1]]
        temp = A[n - 1]

        for i in range(n - 1, -1, -1):

            if temp < A[i]:
                Max.append(A[i])
                temp = A[i]
        return Max

ans = Solution()
A = [16, 17, 4, 3, 5, 2]
print(ans.solve(A))