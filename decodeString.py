# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            # Keep adding to the stack until the ending
            if s[i] != ']':
                stack.append(s[i])
            else:
                # Getting the substring
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                # Case where there is the number, so we multiply the substring with the number
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substr)

        return ''.join(stack)
