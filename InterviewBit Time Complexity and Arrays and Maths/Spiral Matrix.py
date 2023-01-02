class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of list of integers
    def solve(self, A, B, C):
        ans = [([0]*C)for i in range(B)]
        top = 0
        left = 0
        right = C-1
        bot = B-1
        t = 0
        dir = 0
        while(top<=bot and  left<=right):
            if(dir ==0):
                for i in range(left,right+1):
                    ans[top][i] = A[t]
                    t+=1
                top+=1
            elif(dir==1):
                for i in range(top,bot+1):
                    ans[i][right] = A[t]
                    t+=1
                right-=1
            elif(dir==2):
                for i in range(right,left-1,-1):
                    ans[bot][i] = A[t]
                    t+=1
                bot-=1
            elif(dir==3):
                for i in range(bot,top-1,-1):
                    ans[i][left] = A[t]
                    t+=1
                left+=1
            dir = (dir+1)%4
        return ans

ans = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = 3
C = 3
print(ans.solve(A,B,C))