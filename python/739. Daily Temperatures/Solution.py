class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append([t, i])
        return answer
