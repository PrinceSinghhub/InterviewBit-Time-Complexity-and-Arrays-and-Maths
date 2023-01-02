class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def rotate(self, arr, l, item):

        res = []

        for i in range(item, item + l):
            res.append(arr[i % l])

        return res

    def solve(self, A, B):

        ans = []

        for i in range(len(B)):
            temp = self.rotate(A, len(A), B[i])
            ans.append(temp)

        return ans


ans = Solution()
A = [1, 2, 3, 4, 5]
B = [2, 3]
print(ans.solve(A,B))