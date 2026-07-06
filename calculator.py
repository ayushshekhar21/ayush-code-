import ast
import operator
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("360x470")
root.resizable(False, False)

expression = ""

def safe_eval(expr):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
        ast.Mod: operator.mod,
    }

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op = operators[type(node.op)]
            return op(left, right)
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op = operators[type(node.op)]
            return op(operand)
        raise ValueError("Invalid expression")

    parsed = ast.parse(expr, mode='eval')
    return _eval(parsed)


def press(value):
    global expression
    expression += str(value)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def equal():
    global expression
    try:
        if not expression.strip():
            return
        result = safe_eval(expression)
        expression = str(result)
        equation.set(expression)
    except Exception:
        equation.set("Error")
        expression = ""


equation = tk.StringVar()

input_frame = tk.Frame(root, width=340, height=70, bd=0, highlightbackground="black", highlightthickness=1)
input_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

input_field = tk.Entry(
    input_frame,
    font=('Arial', 24, 'bold'),
    textvariable=equation,
    bd=0,
    bg='#f5f5f5',
    justify='right',
    state='readonly',
    readonlybackground='#f5f5f5'
)
input_field.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
input_frame.grid_columnconfigure(0, weight=1)

buttons = [
    ('C', 1, 0, clear, '#f44336'),
    ('⌫', 1, 1, backspace, '#ff9800'),
    ('(', 1, 2, lambda: press('('), '#90caf9'),
    (')', 1, 3, lambda: press(')'), '#90caf9'),
    ('7', 2, 0, lambda: press('7'), '#e0e0e0'),
    ('8', 2, 1, lambda: press('8'), '#e0e0e0'),
    ('9', 2, 2, lambda: press('9'), '#e0e0e0'),
    ('/', 2, 3, lambda: press('/'), '#90caf9'),
    ('4', 3, 0, lambda: press('4'), '#e0e0e0'),
    ('5', 3, 1, lambda: press('5'), '#e0e0e0'),
    ('6', 3, 2, lambda: press('6'), '#e0e0e0'),
    ('*', 3, 3, lambda: press('*'), '#90caf9'),
    ('1', 4, 0, lambda: press('1'), '#e0e0e0'),
    ('2', 4, 1, lambda: press('2'), '#e0e0e0'),
    ('3', 4, 2, lambda: press('3'), '#e0e0e0'),
    ('-', 4, 3, lambda: press('-'), '#90caf9'),
    ('0', 5, 0, lambda: press('0'), '#e0e0e0'),
    ('.', 5, 1, lambda: press('.'), '#e0e0e0'),
    ('%', 5, 2, lambda: press('%'), '#90caf9'),
    ('+', 5, 3, lambda: press('+'), '#90caf9'),
    ('=', 6, 0, equal, '#4caf50'),
]

for text, row, col, command, color in buttons:
    width = 8
    if text == '=':
        button = tk.Button(root, text=text, command=command, bg=color, fg='white', width=34, height=2)
        button.grid(row=row + 1, column=0, columnspan=4, padx=5, pady=5)
    else:
        button = tk.Button(root, text=text, command=command, bg=color, fg='black', width=8, height=2)
        button.grid(row=row + 1, column=col, padx=5, pady=5)

for col in range(4):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()
