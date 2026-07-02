class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=0
        p=str(n)
        for i in range(len(p)):
            digit=int(p[i])
            if i%2==0:
                s+=digit
            else:
                s-=digit
        return s
        