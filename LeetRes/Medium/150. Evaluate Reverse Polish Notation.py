import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = { '+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : 
            operator.truediv}
        stacker = []
        for x in tokens:
            if x.isdecimal() or (x.startswith('-') and x[1:].isdecimal()):
                stacker.append(int(x))
            else:
                num2 = stacker.pop()
                num1 = stacker.pop()
                tmp_num = int(ops[x](num1,  num2))
                stacker.append(tmp_num)
        return stacker.pop()