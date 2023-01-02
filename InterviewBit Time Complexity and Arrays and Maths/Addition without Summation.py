class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def addNumbers(self, A, B):

        # return A+B
        while B:

            carry = A & B

            A = A ^ B

            B = carry << 1

        return A


ans = Solution()
a = 10
b = 3
print(ans.addNumbers(a,b))