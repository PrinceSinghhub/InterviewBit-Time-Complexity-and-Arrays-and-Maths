class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        A = A.split(',')

        ans = []
        for i in A:
            ans.append(int(i))
        return ans
