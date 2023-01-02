class Solution:
    # @param A : tuple of integers
    # @param T : integer
    # @return a list of integers
    def twoSum(self, A, T):
        idxHash = dict()
        output = []
        for i in range(len(A)):
            try:
                output = [idxHash[A[i]]+1, i+1]
                break
            except:
                try:
                    idxHash[T-A[i]]
                    continue
                except:
                    idxHash[T-A[i]] = i

        return output



ans = Solution()
a = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]

b = -3
print(ans.twoSum(a,b))