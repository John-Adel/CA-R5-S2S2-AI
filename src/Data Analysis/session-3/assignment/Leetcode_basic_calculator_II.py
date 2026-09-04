# Challenge: https://leetcode.com/problems/basic-calculator-ii/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        s = s.replace(" ", "")
        numbers = re.split(r"\D", s)
        operators = re.findall(r"\*|/|\+|-", s)
        stack = []
        i = 0
        while True:
            if (operators == [] and numbers != []) or (operators == [] and numbers == []):
                if numbers != [] and operators == []:
                    stack.append(int(numbers.pop(0)))
                if "-" in stack:
                    stack.remove("-")
                    stack.append(stack.pop(0) - stack.pop(0))
                elif "+" in stack:
                    stack.remove("+")
                    stack.append(stack.pop(0) + stack.pop(0))
                break
            if i == 0:
                stack.append(int(numbers.pop(0)))
            if operators[0] == "*":
                operators.remove("*")
                if stack[-1] != "+" and stack[-1] != "-":
                    stack.append(stack.pop() * int(numbers.pop(0)))
                else:
                    stack.append(int(numbers.pop(0)) * int(numbers.pop(0)))
            elif operators[0] == "/":
                operators.remove("/")
                if stack[-1] != "+" and stack[-1] != "-":
                    stack.append(stack.pop() // int(numbers.pop(0)))
                else:
                    stack.append(int(numbers.pop(0)) // int(numbers.pop(0)))
            elif operators[0] == "+":
                if "+" in stack and len(stack) > 2:
                    stack.remove("+")
                    stack.append(stack.pop() + stack.pop())
                elif "-" in stack and len(stack) > 2:
                    stack.remove("-")
                    stack.append(stack.pop(0) - stack.pop(0))
                elif "+" in stack and len(stack) <= 2:
                    stack.remove("+")
                    stack.append(int(numbers.pop(0)) + stack.pop(0))
                elif "-" in stack and len(stack) <= 2:
                    stack.remove("-")
                    stack.append(stack.pop(0) - int(numbers.pop(0)))
                stack.append(operators.pop(0))
            elif operators[0] == "-":
                if "+" in stack and len(stack) > 2:
                    stack.remove("+")
                    stack.append(stack.pop(0) + stack.pop(0))
                elif "-" in stack and len(stack) > 2:
                    stack.remove("-")
                    stack.append(stack.pop(0) - stack.pop(0))
                elif "-" in stack and len(stack) <= 2:
                    stack.remove("-")
                    stack.append(stack.pop(0) - int(numbers.pop(0)))
                elif "+" in stack and len(stack) <= 2:
                    stack.remove("+")
                    stack.append(stack.pop(0) + int(numbers.pop(0)))
                stack.append(operators.pop(0))
            i += 1
        return stack[0]
                