#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    strlen = len(sys.argv)
    if strlen < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == "+":
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
            exit(0)
        elif operator == "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
            exit(0)
        elif operator == "*":
            print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
            exit(0)
        elif operator == "/":
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
