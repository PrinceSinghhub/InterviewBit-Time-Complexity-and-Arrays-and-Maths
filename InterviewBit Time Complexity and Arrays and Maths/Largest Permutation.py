class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        index_array = [0] * (len(A) + 1)
        length = len(A)
        for i in range(len(A)):
            index_array[A[i]] = i

        for i in range(len(A)):
            if B == 0:
                break
            if A[i] != length:
                temp = A[i]
                A[i] = length
                A[index_array[A[i]]] = temp
                index_array[temp] = index_array[A[i]]
                B -= 1
            length -= 1

        return A