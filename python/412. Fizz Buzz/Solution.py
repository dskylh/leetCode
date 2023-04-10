class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return ["FizzBuzz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else "FizzBuzz" if i % 15 == 0 else f"{i}" for i in
                range(1, n)]
