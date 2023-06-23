class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: list[str]):
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + "#" + s
        return ans

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str):
        # write your code here
        ans = []
        for i, s in enumerate(string):
            if s == "#":
                l = int(string[i - 1])
                ans.append(string[i + 1 : i + 1 + l])
        return ans


sol = Solution()
print(sol.decode(sol.encode(["we", "say", ":", "yes"])))
