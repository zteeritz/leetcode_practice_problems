class Solution:
    def valid_parentheses(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and stack.pop() != '(':
                    return False
                if char == ']' and stack.pop() != '[':
                    return False
                if char == '}' and stack.pop() != '{':
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.valid_parentheses("()"))
    print(sol.valid_parentheses("(())"))
    print(sol.valid_parentheses("()[]{}"))
    print(sol.valid_parentheses("(]"))
    print(sol.valid_parentheses("([)]"))
