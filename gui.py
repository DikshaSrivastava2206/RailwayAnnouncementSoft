import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1000x800')
        self.title('Railway Announcement Generator')
        first_label = tk.Label(self, text = "Enter Train Details", font=10)
        first_label.pack(pady= 1, padx = 1)
        first_button = tk.Button(self, text ="Submit", command = hello)
        first_button.pack(pady= 0, padx = 1)
        first_entry = tk.Entry(self, width = 10)
        first_entry.pack(padx = 7, pady = 7)
        first_entry = tk.Entry(self, width=10)
        first_entry.pack(padx=7, pady=7)
        first_entry = tk.Entry(self, width=10)
        first_entry.pack(padx=7, pady=7)
        first_entry = tk.Entry(self, width=10)
        first_entry.pack(padx=7, pady=7)
        first_entry = tk.Entry(self, width=10)
        first_entry.pack(padx=7, pady=7)
        first_entry = tk.Entry(self, width=10)
        first_entry.pack(padx=7, pady=7)

def hello():
    x = first_entry.get()
    print(x)
app = Application()
app.mainloop()