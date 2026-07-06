from tkinter import *
from tkinter import filedialog
import re
import tkinter as tk
from tkinter import ttk
import sys
sys.setrecursionlimit(10000) 


def Lfile():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        inpt.delete("1.0", "end")
        with open(file_path, 'r') as file:
            file_content = file.read()
            inpt.insert("1.0", file_content)
def Rfile():
    try:
        return inpt.get("1.0","end-1c")
    except:
        return None

def evaluate_expression(expression, variable_dictionary):
    try:
        for var, value in variable_dictionary.items():
            expression = expression.replace(var, str(value))
        result = eval(expression)
        return result
    except Exception as e:
        #print(f"Error evaluating expression: {e}")
        return None

def handle_assignment(line, variable_dictionary):
    assignment_match = re.match(r'\s*([a-zA-Z]+)\s*=\s*(.+)', line)
    
    if assignment_match:
        n1 = assignment_match.group(1)
        expression = assignment_match.group(2)

        value = evaluate_expression(expression, variable_dictionary)

        if value is not None:
            variable_dictionary[n1] = value
            print("Variable declared:", n1, "=", variable_dictionary[n1])
        else:
            print("Error evaluating expression in assignment:", expression)
        
def perform_operation(op1, val1, op2, val2):
    if op1 == "+":
        result = val1 + val2
    elif op1 == "-":
        result = val1 - val2
    elif op1 == "*":
        result = val1 * val2
    elif op1 == "/":
        result = val1 / val2 if val2 != 0 else None

    if op2:
        if op2 == "+":
            result += val2
        elif op2 == "-":
            result -= val2
        elif op2 == "*":
            result *= val2
        elif op2 == "/":
            result /= val2 if val2 != 0 else None

    return result

def ulang(string, variable_dictionary):
    global cek
    flag_list = []
    flag_list.append(string)

    # Extract the number of loops from the string
    loop_count_match = re.match(r'ulang (\d+):', string)
    if loop_count_match:
        loop_count = int(loop_count_match.group(1))
    else:
        print("Invalid ulang format:", string)
        return

    for _ in range(loop_count):
        # Execute the code block inside the loop
        for i in flag_list:
            dictionary(i, variable_dictionary)

def untukIF(string,variable_dictionary):
    syarat_if=re.search(r'jika ([a-zA-Z]+)([<>]=?)(\d+)',string)
    if syarat_if:
        global cek
        n1=syarat_if.group(1)
        pembanding=syarat_if.group(2)
        syarat=int(syarat_if.group(3))
        if pembanding== "<":
            cek=variable_dictionary[n1] < syarat
        if pembanding=="<=":
            cek=variable_dictionary[n1] <= syarat
        if pembanding== ">":
            cek=variable_dictionary[n1] > syarat
        if pembanding==">=":
            cek=variable_dictionary[n1] >= syarat
        return cek
def RUN():
    global konten_file
    global input_list
    outpt.delete("1.0", "end")
    konten_file = Rfile()
    input_list = konten_file.strip().split('\n')
    variable_dictionary = {}
    for i in input_list:
        dictionary(i, variable_dictionary)

def untukGOTO(string, variable_dictionary):
    global cek
    goto_statement = re.match(r'goto\s+([a-zA-Z]+)', string)
    if goto_statement and cek:
        label_name = goto_statement.group(1)
        if label_name.endswith(':'):
            label_name = label_name[:-1]  
        if f'{label_name}:' in input_list:
            loop = input_list.index(f'{label_name}:')
            for i in input_list[loop:]:
                dictionary(i, variable_dictionary)
        else:
            print(f"Label not found: {label_name}")

def nyetak(string, variable_dictionary):
    match_double_quotes = re.match(r'nyetak\("([^"]*)",\s*([a-zA-Z]+)\)', string)
    match_single_quotes = re.match(r"nyetak\('([^']*)',\s*([a-zA-Z]+)\)", string)
    match_single_string = re.match(r"nyetak\('([^']*)'\)", string)
    match_variable_only = re.match(r'nyetak\(\s*([a-zA-Z]+)\s*\)', string)
    
    if match_double_quotes:
        content = match_double_quotes.group(1)
        variable_name = match_double_quotes.group(2)
    elif match_single_quotes:
        content = match_single_quotes.group(1)
        variable_name = match_single_quotes.group(2)
    elif match_single_string:
        content = match_single_string.group(1)
        variable_name = ''
    elif match_variable_only:
        variable_name = match_variable_only.group(1)
        content = ''
    else:
        print("Invalid nyetak format:", string)
        return
    
    output_text = f"{content} {variable_dictionary.get(variable_name, '')}\n"
    outpt.insert("end",output_text)

def dictionary(string,variable_dictionary):
    kamus = {
        '=':handle_assignment,
        'ulang:':ulang,
        'jika':untukIF,
        'goto':untukGOTO,
        'nyetak': nyetak,
    }
    for key in kamus:
        if key in string:
            kamus[key](string,variable_dictionary)
            break
def drop_block_lainnya(code_block):
    level = 0
    for i, line in enumerate(code_block):
        if "jika" in line:
            level += 1
        elif "lainnya:" in line:
            if level == 0:
                return code_block[i + 1:]
            else:
                level -= 1
    return []

cek=None
konten_file=[]
input_list=[]

root=tk.Tk()
root.geometry("830x550")

style = ttk.Style()
style.configure("Rounded.TButton", padding=6, relief="flat", background="lightblue")

mainFrame=Frame(root)
mainFrame.grid(column=0,row=0)

inpt=Text(mainFrame, height=15, width=100, borderwidth=5)
inpt.grid(column=0, row=2)


outpt=Text(mainFrame, height=8, width=100, borderwidth=5)
outpt.grid(column=0, row=3)

Compile_Button=ttk.Button(mainFrame, text="Run",style="Rounded.TButton", command=RUN)
Compile_Button.place(x=250,y=480)
Compilee_Button=Button(mainFrame, text="Run", padx=30, pady=20, borderwidth=5, command=RUN)
Compilee_Button.grid(column=3, row=4, sticky=W)

Load_Button = ttk.Button(mainFrame, text="File", style="Rounded.TButton", command=Lfile)
Load_Button.place(x=500,y=480)

#rounded_button = ttk.Button(root, text="Click Me!", style="Rounded.TButton", command=on_button_click)
#rounded_button.pack(pady=20, padx=50)
root.mainloop()