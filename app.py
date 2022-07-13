import tkinter as tk
import pyshorteners

class App:
    def __init__(self, master):
        self.master = master

        # Declare entry, button, and label widgets
        self.entry = tk.Entry(master, width=40)
        self.button = tk.Button(master, text='Go', command=self.shorten)
        self.label = tk.Text(master, width=35, height=1)
            # I used a text widget instead so the user could copy the new link more easily

        # Place widgets on window
        self.entry.grid(row=0, column=0, pady=15, padx=5)
        self.button.grid(row=0, column=1, padx=5)
        self.label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Shorten URL, and place short URL in label widget
    def shorten(self):
        short = pyshorteners.Shortener()
        shorturl = short.tinyurl.short(self.entry.get())
        
        self.label.delete(1.0, tk.END)
        self.label.insert(tk.END, shorturl)

# Initiate window, rename window, show tkinter where my app is, and close window loop :)
def main():
    root = tk.Tk()
    root.title('URL Shortener')

    window = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()