import sys
import traceback

if len(args := sys.argv) > 1:
    print(args)
    target_file: str = args[1]
else:
    target_file: str = "main.txt"

with open(target_file, "r") as FILE:
    code: str = FILE.readlines()

vals: list = [0 for _ in range(len(code))]
current_line: int = 0
index: int = 0
running: bool = True
stack: list = []
feed_mode: str | None = None
call_stack: list = []

try:
    while running:
        instruction = code[current_line][index]
        index += 1
        # print(instruction, end="")
        # print(instruction, stack, vals, feed_mode)

        # feed mode
        if feed_mode is not None:
            if feed_mode == "s": # step
                if instruction == ":":
                    feed_mode = ":"
                    stack.append("")
                elif instruction == "|":
                    feed_mode = None

            elif feed_mode == ":":
                if instruction == ":":
                    feed_mode = "s"
                else:
                    stack[-1] += instruction

            continue

        # quit instruction
        if instruction == "q":
            running = False

        # get user input
        elif instruction == "_":
            stack.append(input("> "))

        # add value to stack
        elif instruction == ":":
            stack.append(code[current_line][index])
            index += 1

        # duplicate top of stack
        elif instruction == "d":
            stack.append(stack[-1])

        # pop
        elif instruction == "/":
            stack.pop()

        # add top 2 stack values
        elif instruction == "+":
            stack.append(stack.pop() + stack.pop())

        # multiplies top 2 stack values
        elif instruction == "*":
            stack.append(stack.pop() * stack.pop())

        # negate number in top of stack
        elif instruction == "-":
            stack.append(-stack.pop())

        # negate number in top of stack
        elif instruction == "&":
            stack.append(1/stack.pop())

        # print top of stack
        elif instruction == ".":
            print(stack[-1])

        # store value in top of stack
        elif instruction == ",":
            vals[current_line] = stack[-1]

        # get value from vals
        elif instruction == "=":
            stack.append(vals[int(stack.pop())])

        # convert top of stack to int
        elif instruction == "i":
            stack.append(int(stack.pop()))

        # convert top of stack to ascii value
        elif instruction == "a":
            stack.append(int(str(stack.pop()).encode().hex(), 16))

        # go down a line
        elif instruction == "v":
            current_line += 1
            index -= 1

        # go down a line and to start of line
        elif instruction == "V":
            current_line += 1
            index = 0

        # go up a line
        elif instruction == "k":
            current_line -= 1
            index -= 1

        # go up a line and to start of line
        elif instruction == "K":
            current_line -= 1
            index = 0

        # jump to line keep index
        elif instruction == "j":
            current_line = int(stack.pop())
            index -= 1

        # jump to index
        elif instruction == "J":
            current_line = int(stack.pop())
            index = 0

        # conditional
        elif instruction == "x":
            if stack[-1] == 0:
                current_line += 1
                index -= 1

        # call
        elif instruction == "c":
            call_stack.append((current_line, index))
            current_line = int(stack.pop())
            index = 0

        # return
        elif instruction == "r":
            current_line, index = call_stack.pop()

        # feed mode
        elif instruction == ">":
            feed_mode = "s"

except Exception as err:
    print(f"error at {current_line},{index}\nstack: {stack}\nline values: {vals}\ninstruction: {instruction}")
    traceback.print_tb(err.__traceback__)