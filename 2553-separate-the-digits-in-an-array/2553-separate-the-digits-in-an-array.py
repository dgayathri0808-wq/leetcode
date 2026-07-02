class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=[]
        for num in nums:
            for digit in str(num):
                s.append(int(digit))
        return s
        