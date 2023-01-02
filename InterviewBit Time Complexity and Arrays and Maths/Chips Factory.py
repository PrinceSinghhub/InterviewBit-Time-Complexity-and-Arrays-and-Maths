class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        zeros = []
        packet = []

        for i in A:
            if i == 0:
                zeros.append(i)
            else:
                packet.append(i)

        return packet+zeros

ans = Solution()
arr = [0,0,0,2,1,4,5,87,10,1]
print(ans.solve(arr))