board = [" "," " , " " , " ",
         
         " " , " " , " ",
         
         " " , " " ," ",]

def display_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

def player1_turn():
    player1_choice = int(input("where do u want place ur x from position(1-9):"))
    board[player1_choice] = "x"

def player2_turn():
    player2_choice = int(input("where do u want place ur o from position(1-9):"))
    board[player2_choice] = "o"

def is_board_full():
    is_board_full = " "
    if board[1] or board[2] or board[3] or board[4] or board[5] or board[6] or board[7] or board[8] or board[9] == " ":
        is_board_full = False
    else:
        is_board_full = True
        win_check()
    
        

def win_check():
    
    if(board[1] == board[2] == board[3] == "x")or(board[4] == board[5] == board[6] == "x") or(board[7] == board[8] == board[9] == "x") or(board[1] == board[4] == board[7] == "x") or(board[2] == board[5] == board[8] == "x") or(board[3] == board[6] == board[9] == "x") or (board[1] == board[5] == board[9] == "x") or(board[3] == board[5] == board[7] == "x"):
        print("x wins the game!!")
        
            
            
    
           


       

    elif (board[1] == board[2] == board[3] == "o") or(board[4] == board[5] == board[6] == "o") or(board[7] == board[8] == board[9] == "o") or(board[1] == board[4] == board[7] == "o") or(board[2] == board[5] == board[8] == "o") or(board[3] == board[6] == board[9] == "o") or(board[1] == board[5] == board[9] == "o") or(board[3] == board[5] == board[7] == "o"):
        print("o won the game!!")
        
    

    

def main_program():

    while is_board_full != True:
        player1_turn()
        display_board()
        win_check()
        if win_check == "x wins the game!!":
            break
        player2_turn()
        display_board()
        win_check()
        if win_check == "o wins the game!!":
            break


print("Welcom to tic tac toe: ")
play_or_not = input("if u want to play press p , to quit press q (p\q): ")



if play_or_not.lower() == "p":
    player1 = input(" enter 1st player name: ")
    print(player1 + " your token is x")
    player2 = input("enter 2st player name: ")
    print(player2 + " your token is o")

    display_board()

    main_program()


else:
    print("thank you for playing!!")

   
                
            
        
        
             
       
       
    
    
    




    

        

        


    
 

   














    
