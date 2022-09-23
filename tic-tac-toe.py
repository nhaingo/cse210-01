'''CSE210 - Week02 code 
Author: Haingotiana Naharivelo'''
def main(): 
#1-create a board with 3 rows and 3 columns, numerated from the number 1 to 9, stored in a variable called board.
    board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    display_board(board)
#create variables for 2 players. The first variable Player1 hold a string value "X" and the second variable Player2 hold a string value "O"
    player1 = "X"
    player2 = "O"
# Player1 and Player2 take turn. Define a function for the current_player() that hold as parameters player1, player2. A third parameter is passed for the start of the game.
# The function current_player should be able to toggle player for each turn
    current = current_player("", player1, player2)
#The function player_input should prompt the current player to enter a specific number form the board. 
#The function takes as parameter the function current_player 
    player_choice = player_input(current)
#Match the number entered by the current player with the number on the board. Replace the number macthed with the string value of the current player with X or O
#The function draw_board() takes as a parameter board, current, and player_choice.add()
 #   draw_board(player_choice, current, board)
 
'''Call the function named "display_board()" that takes as parameter (board)
This function should display the board'''
def display_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} | ", end="")
        print()
        print()
'''Call the function current_player() that takes 3 parameters current, player1 and player2
Use an if block to determine the conditions when the function should switch'''
def current_player(current, player1, player2):
    if current =="" or current == player2:
        return player1
    else:
        return player2 
'''Call the function player_input that take as parameter the variable current. Prompt the user to enter a number from the grill and return the number'''
def player_input(current):    
    number = int(input(f"Player {current}, input a number from the board (1 - 9): ") )
    return number
'''Call the function draw_board and pass 3 parameters: player_choice, current, board. 
Use an if, elif, and else block and return'''
#def draw_board(player_choice, current, board):
    

if __name__ == "__main__":
    main()