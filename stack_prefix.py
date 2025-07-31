def stack(exp):
    operator = []
    operand = []
    priority = {"+":2, "-":2, "*":3, "/":3}
    i = 0
    while(i<len(exp)):
        num = ""
        if(exp[i].isdigit()):
            while (i<len(exp) and exp[i].isdigit()):
                num = num + exp[i]
                i += 1
            operand.append(int(num))
        else:
            while operator and priority[operator[-1]] >= priority[exp[i]]:
                op = operator.pop()
                num2 = operand.pop()
                num1 = operand.pop()
                if op == "+":
                    operand.append(num1 + num2)
                elif op == "-":
                    operand.append(num1 - num2)
                elif op == "*":
                    operand.append(num1 * num2)
                elif op == "/":
                    operand.append(num1 // num2)
            operator.append(exp[i])
            i += 1

    while (operator):
        op = operator.pop()
        num2 = operand.pop()
        num1 = operand.pop()
        if op == "+":
            operand.append(num1 + num2)
        elif op == "-":
            operand.append(num1 - num2)
        elif op == "*":
            operand.append(num1 * num2)
        elif op == "/":
            operand.append(num1 // num2)
    return operand[0]



exp = "10+2*3//4+3"
res = stack(exp)
print(res)
