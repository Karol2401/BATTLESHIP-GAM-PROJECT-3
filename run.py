from random import randint

scores = {"computer": 0, "player": 0}


class Board:

    """
    Main borad class
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
        Function for validating the coordinated.
    """
    if x < 0 or x >= board.size:
        return True
    if y < 0 or y >= board.size:
        return True
    return False


def populate_board(board):
    """
        function for populating the board with ships
    """
    x = random_point(board.size)
    y = random_point(board.size)
    while True:
        if (x, y) in board.ships:
            x = random_point(board.size)
            y = random_point(board.size)
        else:
            break
    if board.type == "computer":
        board.ships.append((x, y))
    else:
        board.ships.append((x, y))
        board.board[x][y] = "@"


def make_guess(board):
    """
        Player and opponent choices.
    """
    # player
    while True:
        if board.type == "player":
            row = int(input("Guess a row: "))
            col = int(input("Guess a column: "))
            if valid_coordinates(row, col, board):
                print(f"Values must be betwen 0 and {board.size - 1}!")
                continue
        else:
            row = random_point(board.size)
            col = random_point(board.size)
        if (row, col) not in board.guesses:
            board.guesses.append((row, col))
            break
        elif board.type == "player":
            print("You can't guess the same coordinates twice!")
    return (row, col)


def play_game(computer_board, player_board):
    """
        Utilizing all the functions defined above.
    """
    while True:
        print(player_board.name + "'s Board")
        player_board.print()

        print(computer_board.name + "'s Board")
        computer_board.print()
        playerRow, playerCol = make_guess(player_board)
        print("Player guessed: ", (playerRow, playerCol))
        playerStatus = player_board.guess(playerRow, playerCol)
        if playerStatus == "Hit":
            scores["player"] += 1
            print("Target hit by player")
        else:
            print("Player missed this time.")

        computerRow, computerCol = make_guess(computer_board)
        print("Computer guessed: ", (computerRow, computerCol))

        computerStatus = computer_board.guess(computerRow, computerCol)
        if computerStatus == "Hit":
            scores["computer"] += 1
            print("Target hit by computer")
        else:
            print("Computer missed this time.")

        if scores["player"] == len(computer_board.ships):
            print("Player Won")
            break
        if scores["computer"] == len(player_board.ships):
            print("computer won")
            break

        flag = input("Enter any key to continue or n to quit: ")
        if flag == "n":
            break


def new_game():

    """
    #Starts a new game.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" BATTLESHIPS GAME!!")
    print(f" Board Size: {size}. number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n ")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

#     print("computer ships: ", computer_board.ships)

    play_game(computer_board, player_board)


new_game()
