class Solution:
    # @param A : string
    # @return an long
    def solve(self, A):

        ans = 0

        flag = True
        for i in A:

            if i.isdigit():
                continue

            else:
                flag = False
                break
        if flag == True:
            return int(A)

        temp = ""
        for i in A:

            if i.isdigit():
                temp += i

            else:
                if len(temp) > 0:
                    ans = ans + int(temp)
                    temp = ""
        if len(temp) > 0:
            ans += int(temp)

        return ans

ans = Solution()
A = "a12b34c"
print(ans.solve(A))
