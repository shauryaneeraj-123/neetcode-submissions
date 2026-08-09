class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        # count will store how many 1-bits we have found

        while n != 0:
            # n & 1 looks at ONLY the last binary bit.
            #
            # Example:
            # n = 1011
            #
            #     1011
            #   & 0001
            #   ------
            #     0001
            #
            # So this gives 1.

            count += n & 1

            # Shift everything one place right.
            #
            # 1011 -> 0101
            #
            # This removes the bit we just checked.
            n >>= 1

        return count