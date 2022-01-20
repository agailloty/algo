import tkinter as tk
window = tk.Tk()
window.title("Industrialiser un modèle de machine learning")
window.geometry('400x400')

a = tk.Label(window ,text = "First Name").grid(row = 0,column = 0)
b = tk.Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = tk.Label(window ,text = "Email Id").grid(row = 2,column = 0)
d = tk.Label(window ,text = "Contact Number").grid(row = 3,column = 0)
a1 = tk.Entry(window).grid(row = 0,column = 1)
b1 = tk.Entry(window).grid(row = 1,column = 1)
c1 = tk.Entry(window).grid(row = 2,column = 1)
d1 = tk.Entry(window).grid(row = 3,column = 1)

btn = tk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()