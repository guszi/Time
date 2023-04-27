mport tkinter as tk

import time

class Clock:

    def __init__(self, root):

        self.root = root

        self.root.title("时钟")

        self.label = tk.Label(root, font=("Helvetica", 32, "bold"), bg="white")

        self.label.pack(fill=tk.BOTH, expand=1)

        self.update_time()

    def update_time(self):

        now = time.strftime("%Y-%m-%d %H:%M:%S")

        self.label.config(text=now)

        self.label.after(1000, self.update_time)

root = tk.Tk()

app = Clock(root)

root.mainloop()
