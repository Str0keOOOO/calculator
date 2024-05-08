import tkinter as tk
import ast

# define fonts
font_result = ("黑体", 24)
font_button = ("黑体", 24)
# create windows
calculator = tk.Tk()
calculator.title("calculator-python")
calculator.geometry("420x400+100+100")
calculator.resizable(0, 0)
# create result label
result = tk.StringVar()
tk.Label(
    calculator,
    textvariable=result,
    font=font_result,
    height=2,
    width=26,
    justify=tk.LEFT,
    anchor=tk.SE,
    bg="#a6e3e9",
).grid(row=1, column=1, columnspan=4)
# create buttons
button_clear = tk.Button(
    calculator, text="C", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_clear.grid(row=2, column=1, padx=4, pady=3)
button_dot = tk.Button(
    calculator, text=".", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_dot.grid(row=2, column=2, padx=4, pady=3)
button_back = tk.Button(
    calculator, text="🠔", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_back.grid(row=2, column=3, padx=4, pady=3)
button_divided = tk.Button(
    calculator, text="÷", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_divided.grid(row=2, column=4, padx=4, pady=3)
button_times = tk.Button(
    calculator, text="x", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_times.grid(row=3, column=4, padx=4, pady=3)
button_plus = tk.Button(
    calculator, text="+", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_plus.grid(row=4, column=4, padx=4, pady=3)
button_minus = tk.Button(
    calculator, text="-", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_minus.grid(row=5, column=4, padx=4, pady=3)
button_equals = tk.Button(
    calculator, text="=", font=font_button, width=5, relief=tk.FLAT, bg="#71c9ce"
)
button_equals.grid(row=6, column=4, padx=4, pady=3)
button_parentheses_l = tk.Button(
    calculator, text="(", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_parentheses_l.grid(row=6, column=1, padx=4, pady=3)
button_parentheses_r = tk.Button(
    calculator, text=")", font=font_button, width=5, relief=tk.FLAT, bg="#cbf1f5"
)
button_parentheses_r.grid(row=6, column=3, padx=4, pady=3)
button_one = tk.Button(
    calculator, text="1", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_one.grid(row=3, column=1, padx=4, pady=3)
button_two = tk.Button(
    calculator, text="2", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_two.grid(row=3, column=2, padx=4, pady=3)
button_three = tk.Button(
    calculator, text="3", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_three.grid(row=3, column=3, padx=4, pady=3)
button_four = tk.Button(
    calculator, text="4", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_four.grid(row=4, column=1, padx=4, pady=3)
button_five = tk.Button(
    calculator, text="5", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_five.grid(row=4, column=2, padx=4, pady=3)
button_six = tk.Button(
    calculator, text="6", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_six.grid(row=4, column=3, padx=4, pady=3)
button_seven = tk.Button(
    calculator, text="7", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_seven.grid(row=5, column=1, padx=4, pady=3)
button_eight = tk.Button(
    calculator, text="8", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_eight.grid(row=5, column=2, padx=4, pady=3)
button_nine = tk.Button(
    calculator, text="9", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_nine.grid(row=5, column=3, padx=4, pady=3)
button_zero = tk.Button(
    calculator, text="0", font=font_button, width=5, relief=tk.FLAT, bg="#e3fdfd"
)
button_zero.grid(row=6, column=2, padx=4, pady=3)


# define function
def button_click(i: str):
    result.set(result.get() + i)


button_one.config(command=lambda: button_click("1"))
button_two.config(command=lambda: button_click("2"))
button_three.config(command=lambda: button_click("3"))
button_four.config(command=lambda: button_click("4"))
button_five.config(command=lambda: button_click("5"))
button_six.config(command=lambda: button_click("6"))
button_seven.config(command=lambda: button_click("7"))
button_eight.config(command=lambda: button_click("8"))
button_nine.config(command=lambda: button_click("9"))
button_zero.config(command=lambda: button_click("0"))
button_divided.config(command=lambda: button_click("/"))
button_times.config(command=lambda: button_click("*"))
button_plus.config(command=lambda: button_click("+"))
button_minus.config(command=lambda: button_click("-"))
button_dot.config(command=lambda: button_click("."))
button_parentheses_l.config(command=lambda: button_click("("))
button_parentheses_r.config(command=lambda: button_click(")"))


def clear():
    result.set("")


button_clear.config(command=clear)


def back():
    str_result = result.get()
    str_result = str_result[:-1]
    result.set(str_result)


button_back.config(command=back)


def equals():
    str_result = result.get()
    try:
        ast_expr = ast.parse(str_result, mode="eval")
    except SyntaxError:
        print("Not an arithmetic statement!")
        result.set("")
        return "Syntax error!"
    for node in ast.walk(ast_expr):
        if isinstance(node, ast.Attribute):
            return "Calculator dose not support attributes!"
    code = compile(ast_expr, str_result, "eval")
    str_result = eval(code, {"__builtins__": {}}, {})
    result.set(str(str_result))


button_equals.config(command=equals)

calculator.mainloop()
