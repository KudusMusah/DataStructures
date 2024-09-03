class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []

        for i in range(1, n+1):
            1, 2, 3, ..., n
        
        while len(arr) > 1:
            i = i + k - 1
            i = i % len(array)
            arr.pop(i)
        
        return arr[0]
        