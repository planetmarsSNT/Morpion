
from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry('500x550')
root.maxsize(500,550)
root.minsize(500,550)

turn = 2 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
stop_list =[] 
root.config(bg='yellow')

def display_board():
    '''The function is used to draw board'''
    print(board[0] + ' | ' + board[1] + ' | ' +board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_winner():
    '''The function used to check winner'''
    
    if board[0] == board[1] ==board[2] and board[0]!='-':
        print(f'{board[0]} is winner')
        stop_list.append('stop')
    elif board[3] == board[4] ==board[5] and board[3]!='-':
        print(f'{board[3]} is winner')
        stop_list.append('stop')
    elif board[6] == board[7] ==board[8] and board[6]!='-':
        print(f'{board[6]} is winner')
        stop_list.append('stop')

    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i]!='-':
            print(f'{board[i]} is winnner')
            stop_list.append('stop')

    
    if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])) and board[4]!='-':
        print(f'{board[4]} is winner')
        stop_list.append('stop')

def check_tie():
    ''''Function for check match is tie or not.'''
    if len(stop_list)==0 and '-' not in board :
        
        print('The match is tie')
        stop_list.append('tie')

def button_player1(button):
    '''This function is used to change the style of button after clicking for X'''
    button.update()
    button['fg'] = 'yellow'
    button['text'] = 'X'
    button['bg'] = 'blue'

def button_player2(button):
    '''This function is used to change the style of button after clicking for player O'''
    button.update()
    button['fg'] = 'yellow'
    button['text'] = 'O'
    button['bg'] = 'red'

def reset_button_style(button):
    '''This fuction will clear all the effects on button when game restart'''
    button.update()
    button['fg'] = 'white'
    button['text'] = '-'
    button['bg'] = 'black'


def clear_list_and_reset_button_text():
    '''This function is used to play game again by setting all the variables to its initial position'''
    
    button_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in range(9):
        reset_button_style(button_list[i]) 
        board[i] = '-' 
    print(board)
    turn_indicator.update()
    turn_indicator['text']= 'A toi de joué joueur 1' 
    stop_list.clear() 



def update_board(position,button):
    b1.update()
    global turn
    
    if turn%2==0:
        
        turn_indicator.update()
        turn_indicator['text'] = 'A toi de joué joueur 2'
        if board[position-1] == '-': 
            button.update()
            button_player1(button) 
            board[position-1] = 'X' 
            check_winner() 
            check_tie() 
            if 'stop' in stop_list : 
                msg.showinfo('gagnant','Bravo joueur 1 a gagné\n Rejoue ? ')
                print(turn)
                clear_list_and_reset_button_text()
            elif 'tie' in stop_list: 
                msg.showinfo('égalité','égalité')
                clear_list_and_reset_button_text()
            else: 
                stop_list.clear()
                turn += 1
        else: 
            msg.showinfo('cette case est deja occupé',"cette case est deja occupé")

    
    elif turn%2!=0:
        
        turn_indicator.update()
        turn_indicator['text'] = 'A toi de joué joueur 1'
        if board[position-1]=='-':
            print('player 2 turn')
            button_player2(button)
            board[position-1] = 'O' 
            check_winner() 
            check_tie() 
            
            if 'stop' in stop_list :
                msg.showinfo('gagnant', 'Bravo joueur 2 a gagné')
                clear_list_and_reset_button_text()
                turn+=1
            elif 'tie' in stop_list:
                msg.showinfo('égalité', 'égalité')
                clear_list_and_reset_button_text()
            else: 
                stop_list.clear()
                turn += 1
        else:
            msg.showinfo('ERREUR',"cette case est deja occupé")


Label(root,text='Jeux du morpion',font='Arial 25 bold',fg='black',bg='orange').pack(pady=4)

turn_indicator = Label(root,text=' A toi de joué joueur 1',font='MVBoli 19 bold')
turn_indicator.pack()

f1 = Frame(root,width=450,height=100,bg='yellow')
f1.pack(pady=10)
b1 = Button(f1,text=board[0],width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(1,b1))
b1.pack(side=LEFT,padx=4)
b2 = Button(f1,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(2,b2))
b2.pack(side=LEFT,padx=4)
b3 = Button(f1,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(3,b3))
b3.pack()

f2 = Frame(root,width=450,height=100,bg='yellow')
f2.pack(pady=10)
b4 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(4,b4))
b4.pack(side=LEFT,padx=4)
b5 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(5,b5))
b5.pack(side=LEFT,padx=4)
b6 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(6,b6))
b6.pack()

f3 = Frame(root,width=450,height=100,bg='yellow')
f3.pack(pady=10)
b7 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(7,b7))
b7.pack(side=LEFT,padx=4)
b8 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(8,b8))
b8.pack(side=LEFT,padx=4)
b9 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(9,b9))
b9.pack()

print("cree par Jules Corneille")


root.mainloop()