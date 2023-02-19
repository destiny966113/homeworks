"""
0x01. [程式能力] 請用 Python 實作數學運算字 parser ，並計算其結果。
例： a = "(2+3) * 2"，要得到 10 。
"""


def parse_and_calc(a: str):
    stack = []
    a += "+"
    operator = "+"
    current_number = 0
    index = 0
    while index < len(a):
        v = a[index]
        if v.isdigit():
            current_number = current_number * 10 + int(v)
        if v in "+-*/":
            if operator == "+":
                stack.append(current_number)
            if operator == "-":
                stack.append(-current_number)
            if operator == "*":
                stack[-1] *= current_number
            if operator == "/":
                tmp = stack.pop()
                stack.append(int(tmp / current_number))
            current_number = 0
            operator = v
        if v == "(":
            j = index
            cnt = 0
            while j < len(a):
                if a[j] == "(":
                    cnt += 1
                if a[j] == ")":
                    cnt -= 1
                if cnt == 0:
                    break
                j += 1
            current_number = parse_and_calc(a[index + 1 : j + 1])
            index = j
        index += 1
    return sum(stack)


if __name__ == "__main__":
    a = "(2+3) * 2"
    assert parse_and_calc(a) == 10
