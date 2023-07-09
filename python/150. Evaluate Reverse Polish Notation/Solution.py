class Solution:
    def evalRPN(self, tokens: list[str]):
        operators = ["+", "-", "/", "*"]
        curr_numbers: list[int] = []
        for t in tokens:
            if t in operators:
                n2 = curr_numbers.pop()
                n1 = curr_numbers.pop()
                match t:
                    case "+":
                        curr_numbers.append(n1 + n2)
                    case "-":
                        curr_numbers.append(n1 - n2)
                    case "/":
                        curr_numbers.append(int(n1 / n2))
                    case "*":
                        curr_numbers.append(n1 * n2)
            else:
                curr_numbers.append(int(t))

        return curr_numbers[0]


sol = Solution()
sol.evalRPN(["4", "13", "5", "/", "+"])
