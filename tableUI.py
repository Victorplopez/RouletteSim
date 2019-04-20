import tkinter as tk

class tableUI:
    def __init__(self):
        self.betAmount = 1  # set to $1 as default
        self.selectedNumbers = list([])
        self.selectedSquares = list([])
        self.lowsBet = (False, 1)  #initialize to $1
        self.highsBet = (False, 1)
        self.evensBet = (False, 1)  #initialize to $1
        self.oddsBet = (False, 1)
        self.redBet = (False, 1)  #initialize to $1
        self.blackBet = (False, 1)
        self.selectedDozens = list([])
        self.selected2to1 = list([])

        self.root = tk.Tk()
        self.root.title('CSCI 154 Roulette Simulator')
        self.root.resizable(0, 0)  # Makes image non-resizable
        self.root.overrideredirect(True) # disable close window button

        self.image = tk.PhotoImage(file="images/euroBoard.png")
        self.label = tk.Label(image=self.image)
        self.label.pack()
#----------------------------- Dollar Amount Buttons ------------------------------------------------------
        self.oneDollarButton = tk.Button(text = '$1', fg ='black', command=lambda n = 1: self.amountToBet(n))
        self.oneDollarButton.place(x = 30, y =100)

        self.fiveDollarButton = tk.Button(text = '$5', fg ='black', command=lambda n = 5: self.amountToBet(n))
        self.fiveDollarButton.place(x = 30, y =150)

        self.tenDollarButton = tk.Button(text = '$10', fg ='black', command=lambda n = 10: self.amountToBet(n))
        self.tenDollarButton.place(x = 28, y =200)

        self.twentyDollarButton = tk.Button(text = '$20', fg ='black', command=lambda n = 20: self.amountToBet(n))
        self.twentyDollarButton.place(x = 28, y =250)

        # self.fiftyDollarButton = tk.Button(text = '$50', fg ='black', command=lambda n = 50: self.amountToBet(n))
        # self.fiftyDollarButton.place(x = 28, y =300)
        #
        # self.hundredDollarButton = tk.Button(text = '$100', fg ='black', command=lambda n = 100: self.amountToBet(n))
        # self.hundredDollarButton.place(x = 25, y =350)
# ----------------------------- Outside Bet Buttons ---------------------------------------------------------
        self.oneTo18Image = tk.PhotoImage(file="images/1-18.png")
        self.oneTo18Button = tk.Button(image=self.oneTo18Image, command=lambda n = True: self.placeLowsHighsBet(n))
        self.oneTo18Button.place(x = 124, y = 114)

        self.nineteenTo36Image = tk.PhotoImage(file="images/19-36.png")
        self.nineteenTo36Button = tk.Button(image=self.nineteenTo36Image, command=lambda n = False: self.placeLowsHighsBet(n))
        self.nineteenTo36Button.place(x = 124, y = 698)

        self.evenImage = tk.PhotoImage(file="images/even.png")
        self.evenButton = tk.Button(image=self.evenImage, command=lambda n = True: self.placeEvenOddsBet(n))
        self.evenButton.place(x = 124, y = 226)

        self.oddImage = tk.PhotoImage(file="images/odd.png")
        self.oddButton = tk.Button(image=self.oddImage, command=lambda n = False: self.placeEvenOddsBet(n))
        self.oddButton.place(x = 124, y = 588)

        self.redImage = tk.PhotoImage(file="images/red.png")
        self.redButton = tk.Button(image=self.redImage, command=lambda n = True: self.placeRedBlackBet(n))
        self.redButton.place(x = 124, y = 346)

        self.blackImage = tk.PhotoImage(file="images/black.png")
        self.blackButton = tk.Button(image=self.blackImage, command=lambda n = False: self.placeRedBlackBet(n))
        self.blackButton.place(x = 124, y = 464)
# ----------------------------- Dozen Buttons ---------------------------------------------------------------
        self.dozenButton = []
        self.dozenImage = []
        for i in range(0, 3):
            self.dozenImage.append(tk.PhotoImage(file="images/dozen" + str(i+1) + ".png"))
            self.dozenButton.append(tk.Button(image=self.dozenImage[i], command=lambda n = i: self.placeDozenBet(n)))

        xCoord = 201
        for i in range(0, 3):
            if (i % 3 == 0):
                yCoord = 130
            elif (i % 3 == 1):
                yCoord = 366
            else:
                yCoord = 605
            self.dozenButton[i].place(x=xCoord, y=yCoord)
# ----------------------------- 2to1 Buttons ---------------------------------------------------------------
        self.twoToOneButton = []
        self.twoToOneImage = []
        for i in range(0, 3):
            self.twoToOneImage.append(tk.PhotoImage(file="images/2to1.png"))
            self.twoToOneButton.append(tk.Button(image=self.twoToOneImage[i], command=lambda n = i: self.place2to1Bet(n)))

        yCoord = 812
        for i in range(0, 3):
            if (i % 3 == 0):
                xCoord = 288
            elif (i % 3 == 1):
                xCoord = 422
            else:
                xCoord = 557

            self.twoToOneButton[i].place(x=xCoord, y=yCoord)
#----------------------------- Number Buttons ---------------------------------------------------------------
        self.numberButton = []
        self.numberImage = []
        for i in range(0, 37):
            self.numberImage.append(tk.PhotoImage(file="images/" + str(i) + ".png"))
            self.numberButton.append(tk.Button(image=self.numberImage[i], command=lambda n = i: self.placeNumberBet(n)))

        self.numberButton[0].place(x=395, y=38)

        yCoord = 102
        for i in range(1, 37):
            if (i % 3 == 1):
                xCoord = 288
                if (i > 1):
                    yCoord += 59
            elif (i % 3 == 2):
                xCoord = 422
            else:
                xCoord = 557
            self.numberButton[i].place(x=xCoord, y=yCoord)
# ----------------------------- Square Buttons ---------------------------------------------------------------
        self.squareButton = []
        self.squareImage = tk.PhotoImage(file="images/dot.png")

        for i in range(0, 22):
            self.squareButton.append(tk.Button(image=self.squareImage, command=lambda n = i: self.placeSquareBet(n)))

        yCoord = 142
        for i in range(0, 22):
            if (i % 2 == 0):
                xCoord = 392
                if (i > 1):
                    yCoord += 60
            else:
                xCoord = 527
            self.squareButton[i].place(x=xCoord, y=yCoord)



    def closeTableWindow(self):
        self.root.destroy()

    def amountToBet(self, amount):
        self.betAmount = amount

    def placeNumberBet(self, number):
        self.selectedNumbers.append((number, self.betAmount))
        self.numberButton[number].configure(bg='yellow')

    def placeSquareBet(self, number):
        self.selectedSquares.append((number, self.betAmount))
        self.squareButton[number].configure(bg='yellow')

    def placeLowsHighsBet(self, option):
        if(option):
            self.lowsBet = (True, self.betAmount)
            self.oneTo18Button.configure(bg='yellow')
        else:
            self.highsBet = (True, self.betAmount)
            self.nineteenTo36Button.configure(bg='yellow')

    def placeEvenOddsBet(self, option):
        if(option):
            self.evensBet = (True, self.betAmount)
            self.evenButton.configure(bg='yellow')
        else:
            self.oddsBet = (True, self.betAmount)
            self.oddButton.configure(bg='yellow')

    def placeRedBlackBet(self, option):
        if(option):
            self.redBet = (True, self.betAmount)
            self.redButton.configure(bg='yellow')
        else:
            self.blackBet = (True, self.betAmount)
            self.blackButton.configure(bg='yellow')

    def placeDozenBet(self, number):
        self.selectedDozens.append((number, self.betAmount))
        self.dozenButton[number].configure(bg='yellow')

    def place2to1Bet(self, number):
        self.selected2to1.append((number, self.betAmount))
        self.twoToOneButton[number].configure(bg='yellow')

    def receiveSelectedNumbers(self):
        return self.selectedNumbers

    def receiveSquareSelections(self):
        return self.selectedSquares

    def receiveLowsSelection(self):
        return self.lowsBet

    def receiveHighsSelection(self):
        return self.highsBet

    def receiveEvensSelection(self):
        return self.evensBet

    def receiveOddsSelection(self):
        return self.oddsBet

    def receiveRedSelection(self):
        return self.redBet

    def receiveBlackSelection(self):
        return self.blackBet

    def receiveSelectedDozens(self):
        return self.selectedDozens

    def receiveSelected2to1(self):
        return self.selected2to1