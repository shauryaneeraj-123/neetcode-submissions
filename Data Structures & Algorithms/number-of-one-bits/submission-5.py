class Solution:
    def hammingWeight(self, n: int) -> int:

        #Approach Sub then add
        count = 0

        while n:
            # n & (n - 1) removes the RIGHTMOST 1-bit from n
            n &= n - 1

            # Since we removed exactly one 1-bit,
            # increase our count by 1
            count += 1

        return count