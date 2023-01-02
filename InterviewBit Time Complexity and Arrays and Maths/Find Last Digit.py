import math
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        base = A[-1]
        Pow = B[-2]+B[-1]

        mod = 4

        if int(Pow) % mod == 0:

            ans = int(base) ** 4

            return ans%10

        else:
            m = int(Pow) % mod
            ans = int(base) ** m
            return ans % 10




ans = Solution()
A = "0174520669358005603046598506479720736793297760682474223148909553942090532954907781068677982335584824"
B = "5421158054975868127102040792138616334158595194152449113616682432094194180103217434896269284568749648"
print(ans.solve(A,B))