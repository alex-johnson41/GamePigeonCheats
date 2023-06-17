import tkinter as tk
from gui import gui

def main():
    root = tk.Tk()
    root.title("window")
    gui.MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
