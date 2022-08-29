import tkinter as tk
import cipher_solver

window = tk.Tk()

text_entry = tk.Entry()
text_entry.pack()

answer_text = tk.StringVar()
answer_text.set('')

answer_label = tk.Label(textvariable=answer_text)
answer_label.pack()

def change_text():
    best_match = cipher_solver.best_match(text_entry.get())
    answer_text.set('Best Match: ' + best_match)

solve_button = tk.Button(text='Solve!', command=change_text)
solve_button.pack(side=tk.TOP)


window.mainloop()