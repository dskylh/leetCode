class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # stack = [0] * len(position)
        car = zip(position, speed)
        car = sorted(car, reverse=True)
        stack = []
        for i, c in enumerate(car):
            time = (target - c[0]) / c[1]
            if i == 0:
                stack.append(time)
            if stack[-1] < time:
                stack.append(time)
        return len(stack)
