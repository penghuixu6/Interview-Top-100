# 给出一个有序的整数数组 A 和有序的整数数组 B ，请将数组 B 合并到数组 A 中，变成一个有序的升序数组
# @param A int整型一维数组 
# @param B int整型一维数组 
# @return void
class Solution:
    def merge(self , A, m, B, n):
        C = []
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        # 如果 A 数组还有剩余元素，直接添加到 C 数组中
        while i < m:
            C.append(A[i])
            i += 1
        # 如果 B 数组还有剩余元素，直接添加到 C 数组中
        while j < n:
            C.append(B[j])
            j += 1
        for i in range(m+n):
            A[i] = C[i]