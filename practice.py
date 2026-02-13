# import tkinter as tk

# def click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = eval(str(entry.get()))
#             entry_var.set(result)
#         except:
#             entry_var.set("Error")
#     elif text == "C":
#         entry_var.set("")
#     else:
#         entry_var.set(entry.get() + text)

# # Create main window
# root = tk.Tk()
# root.title("Calculator")
# root.geometry("300x400")

# # Entry field
# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvar=entry_var, font="Arial 20")
# entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# # Buttons layout
# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"]
# ]

# for row in buttons:
#     frame = tk.Frame(root)
#     for btn_text in row:
#         btn = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RAISED, width=5, height=2)
#         btn.pack(side=tk.LEFT, padx=5, pady=5)
#         btn.bind("<Button-1>", click)
#     frame.pack()

# root.mainloop()
# try:
#     if "apple" is "apple":
#         print("Yes")
#     else:
#         print("No")
# except:
#     print("Hi")

# print("a" is "a")

# l=["Priyanshu",10,20,42]
# print(10 in l)

# if (10==10 and 20==20):
#     print("Yes")
# else:
#     print("No")

print(chr(6))