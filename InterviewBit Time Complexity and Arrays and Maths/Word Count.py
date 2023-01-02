class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        arr = A.split(' ')

        count = 0
        for i in arr:
            if i.isalnum():
                count += 1
        return count
