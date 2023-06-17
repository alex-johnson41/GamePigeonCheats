import tkinter as tk
from GUI import gui

def main():
    root = tk.Tk()
    root.title("window")
    cls = gui.MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
