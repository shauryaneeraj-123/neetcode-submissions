class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Create the answer array.
        # Initially assume every day has no warmer future day.
        result = [0] * len(temperatures)

        # Stack stores indices of days whose answer
        # we haven't found yet.
        stack = []

        # Go through each day.
        for current_day in range(len(temperatures)):

            # While today's temperature is warmer than
            # the temperature at the top of the stack...
            while (
                stack
                and temperatures[current_day] > temperatures[stack[-1]]
            ):

                # Get the previous unresolved day.
                previous_day = stack.pop()

                # Calculate how many days it waited.
                result[previous_day] = current_day - previous_day

            # Today's answer isn't known yet,
            # so add it to the stack.
            stack.append(current_day)

        return result