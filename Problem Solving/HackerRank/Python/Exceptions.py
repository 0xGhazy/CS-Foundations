
# URL: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

n = int(input())
operands = []
for i in range(0, n):
    temp_operands = input("").split(" ")
    operands.append((temp_operands))

for operation_operand in operands:
    try:
        # check for ValueError
        op1 = int(operation_operand[0])
        op2 = int(operation_operand[1])

        print(op1//op2)

    except Exception as message:
        print("Error Code:", message)