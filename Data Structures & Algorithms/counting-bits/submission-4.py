class Solution:
    def countBits(self, n: int) -> list[int]:

        # We need an answer for every number from 0 to n.
        # Therefore, we need n + 1 positions.
        answer = [0] * (n + 1)

        for i in range(1, n + 1):

            # i >> 1 removes the last binary bit.
            #
            # Example:
            # i = 5 = 101
            #
            # 101 >> 1 = 10
            #
            # So 5 >> 1 = 2.

            # ans[i >> 1] gives us the number of 1s
            # WITHOUT the final bit.

            # i & 1 tells us whether the final bit
            # is 0 or 1.

            answer[i] = answer[i >> 1] + (i & 1)

        return answer
