class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        small = 0
        large = 0

        for i in A:

            if i > C:
                large += 1

        for i in B:

            if i < C:
                small += 1

        return max(small, large)


ans = Solution()
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = 4
print(ans.solve(A,B,C))