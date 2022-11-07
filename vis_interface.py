"""DEPRECATED"""

import tkinter as tk
import smart_solve

window = tk.Tk()

text_entry = tk.Entry()
text_entry.pack()

answer_text = tk.StringVar()
answer_text.set('')

answer_label = tk.Label(textvariable=answer_text)
answer_label.pack()

def change_text():
    best_match = smart_solve.smart_solve(text_entry.get())
    answer_text.set('Best Match: ' + best_match)

solve_button = tk.Button(text='Solve!', command=change_text)
solve_button.pack(side=tk.TOP)


window.mainloop()