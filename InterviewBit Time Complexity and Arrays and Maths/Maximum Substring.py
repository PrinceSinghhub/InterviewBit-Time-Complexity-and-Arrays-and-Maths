class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n=0
        for i in range(0,len(A),B):
            str1=A[i:i+B]
            # print(str1)
            n=max(n,str1.count('a'))
        return n

ans = Solution()
a = "a"
b = 39
print(ans.solve(a,b))
