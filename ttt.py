from tkinter import *
from tkinter.font import Font
import random


WIDTH=80
BOX_LINE_COLOUR='#6F7C80'
LINE_COLOUR="#D4D4D4"
POSITIONS_OCCUPIED={(x,y):"unoccupied" for x in [0,1,2] for y in [0,1,2] }
FULL_BOARD=False
BOARD = [[None for i in range(3)] for j in range(3)]
canvas =None
AI=None
HUMAN= None


window =Tk()
app_width,app_height=400,400
screen_width=int((window.winfo_screenwidth()/2)-(app_width/2))-10
screen_height=int((window.winfo_screenheight()/2)-(app_height/2))-10
window.geometry(f"{app_width}x{app_height}+{screen_width}+{screen_height}")
window.resizable(False,False)
window.configure(bg="#282828")



def setupboard():
   """Sets Up The board for tic tac toe."""
   global canvas
   canvas = Canvas(window,bg=window["bg"],width=240,height=240,highlightthickness=0)
   canvas.create_line(80,0,80,240,fill=BOX_LINE_COLOUR,width=3)
   canvas.create_line(160,0,160,240,fill=BOX_LINE_COLOUR,width=3)
   canvas.create_line(0,80,240,80,fill=BOX_LINE_COLOUR,width=3)
   canvas.create_line(0,160,240,160,fill=BOX_LINE_COLOUR,width=3)
   canvas.place(x=80,y=80)
def drawmove(move,row,col):
    """Drawing a O or an X based on input move. 
   
    move: X or O depending on the player
    canvas: canvas on which it will be drawn
    row: row no
    col: col no"""
    centre=[ (col*80+WIDTH/2),(row*80+WIDTH/2)]
    topleftcord=[centre[0]-20,centre[1]-20]
    toprightcord=[centre[0]+20,centre[1]-20]
    bottomleftcord=[centre[0]-20,centre[1]+20]
    bottomrightcord=[centre[0]+20,centre[1]+20]
    if move in ['X','x']:
       canvas.create_line(topleftcord,bottomrightcord,fill=LINE_COLOUR,width=5) #Creates one line
       canvas.create_line(toprightcord,bottomleftcord,fill=LINE_COLOUR,width=5)
    elif move in ['O','o']:
       canvas.create_oval(topleftcord,bottomrightcord,outline=LINE_COLOUR,width=5)
       pass
    POSITIONS_OCCUPIED[(row,col)]="occupied"
    BOARD[row][col] = move.lower()
    check_for_full_board()
def Playerturn():
    """Draw a move where player clicks."""
    
    def draw(event):
      
      row,col=-1,-1
      x,y=event.x,event.y
      if x in range(0,80):
         if y in range(0,80):
            row,col=0,0
         elif y in range(80,160):
            row,col=1,0
         elif y in range(160,240):
            row,col=2,0
      elif x in range(80,160):
         if y in range(0,80):
            row,col=0,1
         elif y in range(80,160):
            row,col=1,1
         elif y in range(160,240):
            row,col=2,1
      elif x in range(160,240):
         if y in range(0,80):
            row,col=0,2
         elif y in range(80,160):
            row,col=1,2
         elif y in range(160,240):
            row,col=2,2  
      if POSITIONS_OCCUPIED[(row,col)] != 'occupied':  
        drawmove(HUMAN,row,col)
        canvas.unbind("<Button-1>")
        result= check_for_winner(BOARD)
        if  result == None:
            computerturn()
        else:
            print_winner(result)
        
      
    canvas.bind("<Button-1>",draw)
def check_for_full_board():
   """Checks Wether the board is full."""
   global FULL_BOARD
   if "unoccupied"  not in POSITIONS_OCCUPIED.values():
       FULL_BOARD = True
def equals(a,b,c):
   """Checks if three positions are x or o."""
   if a == b and b==c and a != None :
      return True
   else:
      return False
def check_for_winner(board):
   """Checks to see if the board is won."""
   WINNER = None
   
   
   #Horizontal and Vertical
   for i in range(3):
      if equals(board[i][0],board[i][1],board[i][2]):
         WINNER = board[i][0]
         
      elif equals(board[0][i],board[1][i],board[2][i]):
         WINNER = board[0][i]
         
   #Diagonal
   if equals(board[0][0],board[1][1],board[2][2]):
      WINNER=board[0][0]
      
   elif equals(board[0][2],board[1][1],board[2][0]):
      WINNER=board[0][2]
      
   if WINNER == None and FULL_BOARD:
      WINNER="-"

   return WINNER
def computerturn():
   """Finds a move using minimax algorithm."""
     
   if AI == 'x':
      bestscore = float('-inf')
   elif AI == 'o':
      bestscore = float('inf')

   bestmove =None
   for i in range(3):
      for j in range(3):
         if BOARD[i][j] == None:
            BOARD[i][j] =AI
            if AI == 'x':
               score = minimax(BOARD,0,False)
               bestscore =max(score,bestscore)
            elif AI == 'o':
               score = minimax(BOARD,0,True)
               bestscore=min(score,bestscore)
            if score == bestscore : bestmove = [i,j]
            BOARD[i][j] =None
   drawmove(AI,*bestmove)
   result= check_for_winner(BOARD)
   if  result == None:
        Playerturn()
   else:
      print_winner(result)
def minimax(board,depth,maximizingPlayer):
   
   result = check_for_winner(board)
   if  result != None :
      if AI=='x':
         if result == AI:
            return  (10-depth)
         elif result == HUMAN:
            return (-10+depth)
         else:
            return 0
      elif AI == 'o':
         if result == AI:
            return  (-10+depth)
         elif result == HUMAN:
            return (10-depth)
         else:
            return 0

   if maximizingPlayer:
      maxscore=float("-inf")
      for i in range(3):
         for j in range(3):
            if board[i][j] == None:
               board[i][j]='x'
               score= minimax(board,depth+1,False)
               maxscore = max(score,maxscore)
               board[i][j]=None
      return maxscore if maxscore != float('-inf') else 0
   else:
      minscore=float("inf")
      for i in range(3):
         for j in range(3):
            if board[i][j]==None:
               board[i][j]='o'
               score = minimax(board,depth+1,True)
               minscore= min(score,minscore)
               board[i][j] = None
      return minscore if minscore != float('inf') else 0

   


def print_winner(winner):
   """Prints the winner."""
   gameover_text = StringVar
   if winner == HUMAN:
      gameover_text="YOU WON!!!"  
   elif winner == AI:
      gameover_text="YOU LOST!!!"
   elif winner=="-":
      gameover_text="IT'S A TIE"
   bigfont = Font(
       family="BungeeSpice",
       size=42,
       weight="bold",
       slant='italic'
       )
   text = Label(window,text=gameover_text,font=bigfont,bg=window["bg"],fg="#e6ba2c",padx=200,pady=200)
   text.pack()
def who_goes_first():
   global AI,HUMAN
   AI= random.choice(['x','o'])
   if AI == 'x':
      HUMAN ='o'
      row,col= random.choice([(i,j) for i in range(3) for j in range(3)])
      drawmove(AI,row,col)
      Playerturn()
   else:
      HUMAN='x'
      Playerturn()

setupboard()
who_goes_first()
window.mainloop()