class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        for i in range (len(A)):
            for j in range (i+1,len(A)):
                A[i][j],A[j][i]=A[j][i],A[i][j]
        return A

ans = Solution()
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(ans.solve(A))