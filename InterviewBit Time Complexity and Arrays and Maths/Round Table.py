class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        fact = 1
        for i in range(2,A+1):
            fact*=i
            fact%=1000000007
        return 2*fact %1000000007


ans = Solution()
a = 4
print(ans.solve(a))