class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position and speed, then sort by position (descending)
        cars = sorted(zip(position, speed), reverse=True)
        
        # Stack to store the times for fleets
        stack = []

        for pos, spd in cars:
            # Calculate the time for this car to reach the target
            time = (target - pos) / spd

            # Check if this car forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        # The number of fleets is the size of the stack
        return len(stack)
