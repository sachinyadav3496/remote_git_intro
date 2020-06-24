#!/usr/local/anaconda3/bin/python
import tkinter as tk

root = tk.Tk()

flag = False

def change_color():
    global flag
    bg = "#eeeeee"
    fg = "#333333"
    if flag:
        fg,bg=bg,fg
        flag = False
    else:
        flag = True
    label.config(fg=fg, bg=bg)
    label.after(1000, lambda : change_color())
label = tk.Label(root, text="Hello World")
label.config(fg='#333333', bg='#eeeeee',
             font=("monospace", 40, "bold"))
label.config(height=10, width=30)
label.pack(fill=tk.BOTH, expand=tk.YES)
exit_button = tk.Button(root, text="exit")
exit_button.config(command=lambda : root.quit())

exit_button.config(fg='red', bg='white', font=('Times', 40, 'bold'))
exit_button.pack(fill=tk.X, expand=tk.YES)

label.after(1000, lambda : change_color())
root.mainloop()
