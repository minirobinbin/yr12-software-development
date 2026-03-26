import tkinter as tk

root = tk.Tk()

root.title("Tk Example")
root.minsize(200,200)
root.maxsize(500,500)
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root.geometry(f"300x300+{screen_width//2-150}+{screen_height//2-150}")

quote = tk.Label(root,text="We made the buttons on the screen look so good you'll want to lick them.").pack()
author = tk.Label(root, text="- Steve Jobs").pack()

image = tk.PhotoImage(file="aqua.png")
tk.Label(root, image=image).pack()

root.mainloop()