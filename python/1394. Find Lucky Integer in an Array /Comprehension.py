class Solution:
    def findLucky(self, arr: list[int]) -> int:
        # just to study comprehensions not a pretty solution by any means
        # but it is kinda cool that you can potentially do this with a one-liner
        # return max([k if k == v else -1 for k, v in {i: arr.count(i) for i in arr}.items()])
        dictionary = {i: arr.count(i) for i in arr}
        solutions = [k if k == v else -1 for k, v in dictionary.items()]
        return max(solutions)
