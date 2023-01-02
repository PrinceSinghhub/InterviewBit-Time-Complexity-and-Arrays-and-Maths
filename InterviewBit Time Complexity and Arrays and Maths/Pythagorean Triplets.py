# User function Template for python3
class Solution:

    def solve(self,A):
        arr = [i for i in range(1,A+1)]
        n = len(arr)

        for i in range(n):
            arr[i] = arr[i] * arr[i]
        arr.sort()
        ans = 0
        for i in range(n - 1, 1, -1):
            b = 0
            c = i - 1
            while (b < c):
                if (arr[b] + arr[c] == arr[i]):
                    ans+=1
                    b += 1
                    c -= 1
                else:
                    if (arr[b] + arr[c] < arr[i]):
                        b += 1
                    else:
                        c -= 1
        return ans


ans = Solution()
print(ans.checkTriplet(5))