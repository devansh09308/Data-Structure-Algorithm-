class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while k > 0 and stack and ch < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"