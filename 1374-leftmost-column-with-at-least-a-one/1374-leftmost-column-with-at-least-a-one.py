# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        ans = float('inf')

        for row in range(n):
            l, r = 0, m - 1

            while l <= r:
                mid = (l + r) // 2

                if binaryMatrix.get(row, mid) == 0:
                    l = mid + 1
                else:
                    r = mid - 1
            
            ans = min(ans, l)
        
        return ans if ans < m else -1
                


        
