import tkinter as tk
from Anagrams_Solver import anagrams_solver as aSolver
from WordBites_Solver import wordbites_solver as wbSolver
from WordHunt_Solver import wordhunt_solver as whSolver

class MainWindow():
    def __init__(self, master):
        self.master = master
        master.config(background="green")
        master.geometry("800x500")
        master.title("Game Pigeon Solver")
        label = tk.Label(
            text="GamePigeon Solver", 
            font=("Ariel", 40),
            background="Green",
            
            )

        frm_buttons = tk.Frame(master, background="green")

        btn_anagrams = tk.Button(frm_buttons,text="Anagrams", font=("Ariel", 20), command= self.clk_anagrams)
        btn_wordHunt = tk.Button(frm_buttons,text="Word Hunt",font=("Ariel", 20),command= self.clk_wordhunt)
        btn_wordBites = tk.Button(frm_buttons,text="Word Bites",font=("Ariel", 20), command= self.clk_wordbites)
        
        
        label.pack(pady=50)
        btn_anagrams.grid(row = 0, column=0, padx= 10)
        btn_wordHunt.grid(row=0,column=1,padx= 10)
        btn_wordBites.grid(row=0, column=2,padx= 10)
        
        frm_buttons.pack()


    def clk_anagrams(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = Anagrams(toplevel, "Anagrams")
    
    def clk_wordhunt(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = WordHunt(toplevel, "Word Hunt")
    
    def clk_wordbites(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = WordBites( toplevel, "WordBites")

class WordGame: 
    def __init__(self, master, gameName):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.master.config(background = "green")
        self.master.geometry("800x500+30+10")

        header = tk.Label(
            self.frame,
            text=gameName, 
            font=("Ariel", 40),

            )

        quitButton = tk.Button(self.frame, text = 'Back', width = 25, command= lambda: self.close_windows(), pady=3)
        header.grid(row = 0, column=1)
        quitButton.grid(row=1, column =1)
        self.frame.pack()
        self.master.protocol("WM_DELETE_WINDOW", self.close_windows)
    
    def close_windows(self):
        self.master.destroy()
        self.master.master.deiconify()

class Anagrams(WordGame):

    def __init__(self, master,gameName):
        super().__init__(master,gameName)
        self.words = []
        self.inp = tk.Entry(self.frame)
        self.inp.bind('<Return>',lambda x: self.hitEnter(self))
        lbl_entryLabel = tk.Label(
            self.frame,
            text="Enter all 6 letters with no spaces",
            font=("Arial", 14),
            width= 25
            )
        lbl_fillSpace = tk.Label(
            self.frame, 
            width=25,
            text="Enter: Process Input",
            justify= "left",
            font=("Arial", 14)
            )

        lbl_fillSpace.grid(row=2, column = 2)
        self.inp.grid(row=2, column=1)
        lbl_entryLabel.grid(row=2,column=0)

   
    def hitEnter(event, self):
        test = aSolver.Anagrams_Solver(self.inp.get())
        self.words = test.solve()
        txtBox = tk.Text(
            self.frame, 
            font=("Arial", 20),
            width=10,
            height=14
        )
        for word in self.words:
            txtBox.insert("end", word + "\n")
        txtBox.grid(row=3,column=1)


class WordHunt(WordGame):

    def __init__(self, master,gameName):
        super().__init__(master,gameName)    
        self.words = {}
        self.inp = tk.Entry(self.frame)
        self.currentWord = tk.Label(
            self.frame,
            text="",
            font=("Arial",20)
        )
        lbl_entryLabel = tk.Label(
            self.frame,
            text="Enter all 16 letters with no spaces, \nleft to right, top to bottom",
            font=("Arial", 14),
            width= 29
            )
        lbl_fillSpace = tk.Label(
            self.frame, 
            width=29,
            text="Enter: Process Input and show board\nSpace: Cycle words",
            justify= "left",
            font=("Arial", 14)
            )
        self.inp.bind('<Return>',lambda x: self.hitEnter(self))
        self.inp.bind('<space>', lambda x: self.hitSpace(self))
        self.inp.grid(row=2, column = 1)
        self.currentWord.grid(row=3,column = 1)
        lbl_entryLabel.grid(row=2, column = 0)
        lbl_fillSpace.grid(row=2, column =2)
        


    def printWords(self):
        txtBox = tk.Text(self.frame, font=("Arial",20))
        for key, value, in self.words.items():
            txtBox.insert("end",key+"\n")
        txtBox.pack()

    def hitEnter(event, self):
        test = whSolver.WordHunt_Solver(self.inp.get())
        self.words = test.solve()
        self.createGameGrid()
        #self.printWords()

    def hitSpace(event, self):
        pair = self.words.popitem()
        map = pair[1]
        word = pair[0]
        self.currentWord.config(text=word)
        
        for i in range(4):
            for j in range(4):
                self.gridDict[(i,j)].config(background="Grey")
                if map[i][j] == 1:
                    self.gridDict[(i,j)].config(background="Green")
                if map[i][j] == 2:
                    self.gridDict[(i,j)].config(background="#a68d02")
                if map[i][j] == 3:
                    self.gridDict[(i,j)].config(background="Red")
                
        

    def createGameGrid(self):
        self.gameFrame = tk.Frame(self.frame, pady="15")
        self.gridDict = {}
        counter = 0
        for i in range(4):
            for j in range(4):
                lbl_letter = tk.Label(
                    self.gameFrame,
                    text= self.inp.get()[counter],
                    font=("Ariel", 25),
                    padx="15",
                    pady="5",
                    relief="raised",
                    width="1",
                    height="1",
                    background="gray"
                )
                lbl_letter.grid(row=i, column=j)
                counter += 1
                self.gridDict[(i,j)] = lbl_letter
        self.gameFrame.grid(row=4, column = 1)
    


class WordBites(WordGame):
    def __init__(self, master,gameName):
        super().__init__(master,gameName)
        self.words = []
        self.sLetters = tk.Entry(self.frame)
        self.hLetters = tk.Entry(self.frame)
        self.vLetters = tk.Entry(self.frame)
        self.vLetters.bind('<Return>',lambda x: self.hitEnter(self))
        self.sLetters.grid(row=2, column = 1)
        self.hLetters.grid(row=3, column = 1)
        self.vLetters.grid(row=4, column = 1)
        lbl_sEntry = tk.Label(
            self.frame,
            text="Enter single letters, no spaces",
            font=("Arial", 14),
            width= 29,
            justify="left",
            pady=10
            )
        lbl_hEntry = tk.Label(
            self.frame,
            text="Enter horizontal pairs, no spaces",
            font=("Arial", 14),
            width= 29,
            justify="left",
            pady=10
            )
        lbl_vEntry = tk.Label(
            self.frame,
            text="Enter vertical pairs, no spaces",
            font=("Arial", 14),
            width= 29,
            justify="left",
            pady=10
            )
        lbl_sEntry.grid(row=2, column= 0)
        lbl_hEntry.grid(row=3, column= 0)
        lbl_vEntry.grid(row=4, column= 0)
        lbl_fillSpace = tk.Label(
            self.frame, 
            width=25,
            text="Enter: Process input when\nall letters have been entered",
            justify= "left",
            font=("Arial", 14)
            )
        lbl_fillSpace.grid(row=2,column =2)

    def hitEnter(event, self):
        test = wbSolver.Wordbites_Solver(self.sLetters.get(),self.hLetters.get(),self.vLetters.get())
        self.words = test.solve()
        txtBox = tk.Text(self.frame, font=("Arial", 20), width = 30, height = 10)
        for word in self.words:
            txtBox.insert("end", word + "\n")
        txtBox.grid(row=5, column = 0,columnspan=3)
