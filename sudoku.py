# CSCE 160-Prof. Kim-HW6
#Names: Rares-Mihail Neagu, Tyler Fortune
#Dates:12/6/2021,12/8/2021,12/9/2021
# Sudoku w/ file use
import random 
import sys, os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#--------------CLASSES DEFINITION----------------------------------
class Sudoku:
    def __init__(self, fileName=None):
        #create the boards
        self.origBoard = [None] * 9  # Used to mark original puzzle state
        self.board = [None] * 9      # Used to mark user-entered numbers
        for i in range(9):
            self.board[i] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            self.origBoard[i] = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        #choose the puzzle
        if (fileName==None):  # default puzzle
            self.default()
        else:                 # create puzzle
            self.readFile(fileName)
        #create a unified board by merging the two boards
        self.allBoard=[0]*9
        for i in range(9):
            self.allBoard[i]=[" "]*9
        #fill the unified board
        for i in range(9):
            for j in range(9):
                if(self.board[i][j]==" " and self.origBoard[i][j]==" "):
                    self.allBoard[i][j]=" "
                elif(self.board[i][j]==" "):
                    self.allBoard[i][j]=int(self.origBoard[i][j])
                elif(self.origBoard[i][j]==" "):
                    self.allBoard[i][j]=int(self.board[i][j])
            
    def readFile(self, fn):    
        #fileformat
        #9 lines of original puzzle state
        #9 lines of user entered values
        #Use 0 for empty space       
        #setup file to open
        file = open(os.path.join(__location__,fn), 'r')
        
        #read data as an array of strings
        data = file.readlines()
        #treat the array of strings as a matrix of characters
        #First, process the portion that belongs to the original board
        for i in range(9):
            for j in range(9):
                if (data[i][j]!= '0'):
                    self.origBoard[i][j] = data[i][j]
                    
                    
        #Then, process the user entered values
        for i in range(9,18): #row index 9~17
            for j in range(9):
                if (data[i][j]!= '0'):
                    self.board[i-9][j] = data[i][j]
        
        #close the file
        file.close()
        
    def default(self):
        #user did not provide a puzzle so we will provide one
        #c - choice of level
        self.origBoard[0]=' 19374652'
        self.origBoard[1]='576182943'
        self.origBoard[2]='342596718'
        self.origBoard[3]='921753864'
        self.origBoard[4]='638419527'
        self.origBoard[5]='457628139'
        self.origBoard[6]='185237496'
        self.origBoard[7]='763941285'
        self.origBoard[8]='29486537 '
                 
    def display(self):
        #combine original board and current board
        db = [None] * 9
        for i in range(9):
            db[i] = [None] * 9
            for j in range(9):
                if (self.origBoard[i][j] == ' '):
                    db[i][j] = ' ' + str(self.board[i][j])
                else:
                    db[i][j] = '*' + str(self.origBoard[i][j])
        #format and print
        print("   0  1  2  3  4  5  6  7  8")
        print(" \u2554\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2566\u2550\u2550\u2564\u2550\u2550\u2564\u2550\u2550\u2557")
        i=0
        for m in range(0,3):
            for k in range(0,2):
                print(i,"\u2551",sep='',end='')
                for j in range(0,9,3):
                    print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
                print("")
                print(" \u255F\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u256B\u2500\u2500\u253C\u2500\u2500\u253C\u2500\u2500\u2562")
                i+=1
            print(i,"\u2551",sep='',end='')
            for j in range(0,9,3):
                print(db[i][j], db[i][j+1], db[i][j+2], sep='\u2502', end='\u2551')
            print("")
            if (m<2):
                print(" \u255F\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u256C\u2550\u2550\u256A\u2550\u2550\u256A\u2550\u2550\u2562")
            else:
                print(" \u255A\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u2569\u2550\u2550\u2567\u2550\u2550\u2567\u2550\u2550\u255D")
            i+=1
            
    def saveGame(self, fileName=None):
        if (fileName==None):
            print("You must provide a file name so we can save the game!")
        else:
            print("Saving to:", fileName)
            #open file (for writing)
            file = open(os.path.join(__location__,fileName), 'w')
            #process origBoard and board and write it to the file
            for i in range(9):
                for j in range(9):
                    if(self.origBoard[i][j]!=' '):
                        file.write(self.origBoard[i][j])
                    else:
                        file.write('0')
                file.write("\n")
            for i in range(9):
                for j in range(9):
                    if(self.board[i][j]!=' '):
                        file.write(str(self.board[i][j]))
                    else:
                        file.write('0')
                file.write("\n")     
            #close file
            file.close()

    def UserInput(self,control):
        #this function takes the input from the user
        #it returns the input in an array called choice
        #the control is used to change if the full space and value are aked
        #thus, when the control is not one, only the coordinates are asked
        #control=0(coordinates), control=1(all),control=2(number)
        choice=[None]*3#create an array
        try:
            if(control==1 or control==2):
                if(control==2):
                    choice[0]=int(input("Enter the new number:"))
                else:
                    choice[0]=int(input("Enter a number between 1 and 9:"))
                while(choice[0]>9 or choice[0]<1):#force a valid choice
                    choice[0]=int(input("Enter a valid number between 1 and 9:"))
            else:
                choice[0]=0
            if(control==1 or control==0):
                choice[1]=int(input("Enter the row:"))
                while(choice[1]>8 or choice[1]<0):#force a valid choice
                    choice[1]=int(input("Enter a valid row:"))
                choice[2]=int(input("Enter the column:"))
                while(choice[2]>8 or choice[2]<0):#force a valid choice
                    choice[2]=int(input("Enter a valid column:"))
            if(control==1):
                while(self.CheckFullSpace(choice[1],choice[2])==True):#it is full so it must be reassigned
                    print("-------------------------------------------")
                    print("The spot is already full.Choose another one")
                    choice[0]=int(input("Enter a number between 1 and 9:"))
                    while(choice[0]>9 or choice[0]<1):#force a valid choice
                        choice[0]=int(input("Enter a valid number between 1 and 9:"))
                    choice[1]=int(input("Enter the row:"))
                    while(choice[1]>8 or choice[1]<0):#force a valid choice
                        choice[1]=int(input("Enter a valid row:"))
                    choice[2]=int(input("Enter the column:"))
                    while(choice[2]>8 or choice[2]<0):#force a valid choice
                        choice[2]=int(input("Enter a valid column:"))           
            return choice
        except:
            return self.UserInput(self)

    def CheckValidPlacement(self,a,i,j):
        #this function takes in the gameboard,the chosen number,and its position
        #this function checks if a specific number can be placed
        #depending on the presence of that number in the row, column, or box
        #it returns the validity
        valid=True#create a flag to keep track if the position is valid
        #1.check the column of the chosen value
        for p in range(9):
            if(self.allBoard[p][j]==a):#checks if the value is found in the column
               valid=False#the values has been found
               break
        #2.checks the row of the chosen value
        if(valid==True):
            for k in range(9):
                if(self.allBoard[i][k]==a):#checks if the value is found in the row
                   valid=False#the values has been found
                   break
        #3.check the box of the chosen value
        if(valid==True):
            #3.1 finding the box of x
            #k and p will be used to store the starting point(3k,3p) and to keep track of the box
            #(k,p)00=box 1, 01=box 2 ,and so on
            #3.1.1 finding k and p, finding the box
            k=0#initialize it to 0
            while(i>=0):
                i=i-3
                k=k+1#keeping track how many times it is subtracted
            k=k-1#subtract one to find 1/3 of the starting point
            p=0#initialize it to 0
            while(j>=0):
                j=j-3
                p=p+1#keeping track how many times it is subtracted
            p=p-1
            #3.scan the box to see if it can be found
            for c in range(3*k,3*k+3):
                for d in range(3*p,3*p+3):
                    if(self.allBoard[c][d]==a):#checks if the value is found in the box
                       valid=False#the values has been found
                       break
                if(valid==False):
                    break
        return valid

    def CheckFullSpace(self,i,j):
        #this function checks if the chosen space is full
        #it returns if the spot is full or not
        full=False
        if(self.allBoard[i][j]!=" "):
            full=True#the spot is full
        return full
    def CheckFullBoard(self):
        #this function checks if the board is full
        #and it returns a flag
        full=True
        for i in range(9):
            for j in range(9):
                if(self.allBoard[i][j]==" "):
                    full=False
                    break
        return full
            
    def placementReassignment(self,a,i,j,control):
        #this function takes in the gameboard,the chosen value, and its position
        #it assigns the placement
        x=[" "]*3
        x[0]=a
        x[1]=i
        x[2]=j
        while(self.CheckValidPlacement(x[0],x[1],x[2])==False):
            print("There must be just one instance of each number in each column, row, and box")
            print("---------------------------------------------------------------------------")
            print("Please, try another spot!")
            x=self.UserInput(control)
            if(control==2):
                x[1]=i
                x[2]=j
            if(control==0):
                x[0]=a
        return x
#----------OTHER FUNCTIONS-------------------------------------------------
def userChoice():
    #this function returns the choice of the user in the form of an integer
    try:
        choice=int(input("Enter your choice:"))
        return choice
    except:
        return userChoice()
#---------MAIN FUNCTION----------------------------------------------------   
def main():
    #create a flag to control the flow of the game
    flag=True
    #print the initial menu
    print("-------MENU-------")
    print("1.Start a new game")
    print("2.Load a save")
    print("------------------")
    choice1=userChoice()
    if(choice1==1):
        f=None
    elif(choice1==2):
        f=input("Enter the name of your saved file:")
    #create the game
    try:    
        game=Sudoku(fileName=f)
    except:
        print("---------------------------")
        print("That file does not exist...")
        print("Loading default puzzle.")
        game=Sudoku()
    #the gameplay
    while(True):
        if(flag==True):
            game.display()
            #takes the input from the user
            x=game.UserInput(1)
            x=game.placementReassignment(x[0],x[1],x[2],1)#reassigns to a valid place
            #assign the value to the user matrix and to the unified one
            game.allBoard[x[1]][x[2]]=x[0]
            game.board[x[1]][x[2]]=x[0]
            #check the win condition
            if(game.CheckFullBoard()):
                print("-----------------------")
                print("Congratulation.You won!")
                break
            flag=False
        #print the end of turn menu
        if(flag==False):
            flag=True
            game.display()
            print("-------------MENU---------------")
            print("1.Continue")
            print("2.Save")
            print("3.Overwrite a number you entered")
            print("--------------------------------")
            choice2=userChoice()
            if(choice2==2):
                fn=input("Enter file name:")
                game.saveGame(fn)
                break
            elif(choice2==3):
                print("--------------------------------------------")
                print("Enter which number you would like to change.")
                x=game.UserInput(0)
                #check if the space is full
                if(game.CheckFullSpace(x[1],x[2])==True):
                    #check if it's from the user's choices
                    if(game.board[x[1]][x[2]]!=" "):
                        y=game.UserInput(2)
                        y=game.placementReassignment(y[0],x[1],x[2],2)#reassigns to a valid one
                        #assign the value to the user matrix and to the unified one
                        game.allBoard[x[1]][x[2]]=y[0]
                        game.board[x[1]][x[2]]=y[0]
                    else:
                        if(game.origBoard[x[1]][x[2]]!=" "):
                            print("--------------------------------------------")
                            print("You can not replace numbers from the puzzle!")
                        else:
                            print("--------------------------------------------")
                            print("The place is empty!")
                    flag=False
#--------------MAIN PROGRAM----------------------------------- 
main()






