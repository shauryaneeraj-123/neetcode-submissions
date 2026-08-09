class Solution:
    def countBits(self, n: int) -> list[int]:

        # We need answers for:
        # 0, 1, 2, ..., n
        #
        # So we create n + 1 spaces.
        answer = [0] * (n + 1)

        for i in range(1, n + 1):

            # i >> 1 removes i's final binary bit.
            #
            # Example:
            # 5 = 101
            # 5 >> 1 = 10 = 2
            #
            # answer[i >> 1] tells us how many
            # 1-bits remain after removing the last bit.

            # i & 1 tells us whether the removed
            # final bit was 0 or 1.
            #
            # Therefore:
            # bits in i =
            # bits in i without last bit
            # + last bit

            answer[i] = answer[i >> 1] + (i & 1)

        return answer