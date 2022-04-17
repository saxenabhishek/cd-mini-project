from parser import Parser
import turtle

inputfile = "1.txt"

data = Parser(f"input/{inputfile}").read_all()


def run_instruction(t):
    if t.data == "change_color":
        print(t.children)
        turtle.color(*t.children)  # We just pass the color names as-is

    elif t.data == "movement":
        name, number = t.children
        {"f": turtle.fd, "b": turtle.bk, "l": turtle.lt, "r": turtle.rt,}[
            name
        ](int(number))

    elif t.data == "repeat":
        count, block = t.children
        for i in range(int(count)):
            run_instruction(block)

    elif t.data == "fill":
        turtle.begin_fill()
        run_instruction(t.children[0])
        turtle.end_fill()

    elif t.data == "code_block":
        for cmd in t.children:
            run_instruction(cmd)
    else:
        raise SyntaxError("Unknown instruction: %s" % t.data)


for i in data.children:
    print(i)
    run_instruction(i)
