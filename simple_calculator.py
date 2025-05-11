import tkinter as tk
#hello_world_01
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to display the expression
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief=tk.RIDGE, border=1)
        btn.pack(side='left', expand=True, fill='both', ipadx=5, ipady=10)
        btn.bind("<Button-1>", click)

# Start the GUI loop
root.mainloop()
