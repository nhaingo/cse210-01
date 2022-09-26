'''CSE210 - Week02 code 
Author: Haingotiana Naharivelo'''
def main(): 
#create variables for 2 players. The first variable Player1 hold a string value "X" and the second variable Player2 hold a string value "O"
    player1 = "X"
    player2 = "O"
#-create a board with 3 rows and 3 columns, numerated from the number 1 to 9, stored in a variable called board.
    board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    display_board(board)

# Player1 and Player2 take turn. Define a function for the current_player() that hold as parameters player1, player2. A third parameter is passed for the start of the game.
# The function current_player should be able to toggle player for each turn.
    current = current_player("", player1, player2)
#The function player_input should prompt the current player to enter a specific number form the board. 
#The function takes as parameter the function current_player 
    player_choice = player_input(current)
#Match the number entered by the current player with the number on the board. Replace the number macthed with the string value of the current player by X or O
#The function draw_board() takes as a parameter board, current, and player_choice
    draw_board(player_choice, current, board)
    #display_board(board)
#After each turn, the board should be checked to verify if there's a win. The function check_win() will take the parameter as board

    check_win(board)
#After each turn, the board should be checked to verify if there are unchecked slots. The function checked_slot() will take as paramaters board, player1 and player2.
    checked_slot(board, player1, player2)
#Toggle to next player if check_win is false or if it's checked_slot is false
    while not (check_win(board) or checked_slot(board, player1, player2)):
        display_board(board)
        current = current_player(current, player1, player2)
        player_choice = player_input(current)
        draw_board(player_choice, current, board)
        
#Check and display a message if there is a winner. Then the game stop.
    while check_win(board) == True:
        display_board(board)
        print ("We have a win! Game is Over! Thanks for playing")
        break
#The following while condition is to print a message if there is no winner and all the slots are filled.
    while((check_win(board)==False) and (checked_slot(board, player1, player2)==True)):
        display_board(board)
        print("We have a draw game. Please refresh the game if you want to play again")
        break  
'''Call the function named "display_board()" that takes as parameter (board)
This function should display the board'''
def display_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} | ", end="")
        print()
        print()
'''Call the function current_player() that takes 3 parameters current, player1 and player2
Use an if block to determine the conditions when the players should switch'''
def current_player(current, player1, player2):
    if current == "" or current == player2:
        return player1
    else:
        return player2 
'''Call the function player_input that take as parameter the variable current. Prompt the user to enter a number from the grill and return the number'''
def player_input(current):    
    number = int(input(f"Player {current}, input a number from the board (1 - 9): "))
    return number
'''Call the function draw_board and pass 3 parameters: player_choice, current, board. 
Use an if, elif, and else block and return'''
def draw_board(player_choice, current, board):
    if board[0][0] == player_choice:
        board[0][0] = current
    elif board[0][1] == player_choice:
        board[0][1] = current
    elif board[0][2] == player_choice:
        board[0][2] = current
    elif board[1][0] == player_choice:
        board[1][0] = current
    elif board[1][1] == player_choice:
        board[1][1] = current
    elif board[1][2] == player_choice:
        board[1][2] = current
    elif board[2][0] == player_choice:
        board[2][0] = current
    elif board[2][1] == player_choice:
        board[2][1] = current
    elif board[2][2] == player_choice:
        board[2][2] = current
    else:
        return False  
'''Call the function check_win() to see if the game stop or continue to next player. The function has 1 parameter board and return'''
def check_win(board):
    return(board[0][0] == board[0][1] == board[0][2] or
        board[1][0] == board[1][1] == board[1][2] or
        board[2][0] == board[2][1] == board[2][2] or
        board[0][0] == board[1][0] == board[2][0] or
        board[0][1] == board[1][1] == board[2][1] or
        board[0][2] == board[1][2] == board[2][2] or
        board[0][0] == board[1][1] == board[2][2] or
        board[0][2] == board[1][1] == board[2][0])
'''Call the function checked_slot that take 3 parameters: board, player1, player2 and return. For loop is used to iterate each slot in each row.
The function return true if each slot in each row is X or O'''
def checked_slot(board, player1, player2):
    for row in board:
        for slot in row:
            if slot != player1 and slot != player2:
                return False
    return True


if __name__ == "__main__":
    main()