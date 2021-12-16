class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.player = {}
    def choose_player(self):
        self.player[self.name] = self.token
        print(self.player)
        return self.player
class Game:
    def __init__(self):
        self.board = [' ' , ' ' , ' ' ,
            ' ' , ' ' , ' ' ,
            ' ' , ' ' , ' ' ]
        self.win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        self.moves_count = 0
    def print_board(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
    def p1(self):
            try:
                print(user_1.name)
                move = int(input(f"Type where your {play_1_choice} should be placed\n"))
                if self.board[move] != play_1_choice and self.board[move] != play_2_choice:
                    self.board[move] = play_1_choice
                    self.print_board()
                    self.moves_count += 1
                else:
                    print("That spot is taken")
                    self.p1()
                self.check_win()
            except ValueError:
                print("Write a NUMBER from 0 to 8")
                self.p1()
    def p2(self):
        try:
            print(user_2.name)
            move = int(input(f"Type where your {play_2_choice} should be placed\n"))
            if self.board[move] != play_1_choice and self.board[move] != play_2_choice:
                self.board[move] = play_2_choice
                self.print_board()
                self.moves_count += 1
            else:
                print("That spot is taken")
                self.p2()
            self.check_win()
        except:
            print("Write a NUMBER from 0 to 8")
            self.p2()
    def check_win(self):
        for a in self.win_conditions:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == play_1_choice:
                print(f'{play_1_name} wins!')
                self.play_again()
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == play_2_choice:
                print(f'{play_2_name} wins!')
                self.play_again()
            elif self.moves_count == 9:
                print('A DRAW!')
                exit()
    def play(self):
        while True:
            self.p1()
            self.p2()
    def run(self):
        self.print_board()
        self.play()
    def play_again(self):
        while True:
            question = input("Do you want to play again? Type y or n\n")
            if question == "y":
                print("\nLet's play!")
                self.board = [' ' , ' ' , ' ' ,
                               ' ' , ' ' , ' ' ,
                                  ' ' , ' ' , ' ' ]
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Thats not a valid option")
# Program
play_1_name = input('\nWhat is your name player 1: ')
play_1_choice = input("\nAre you X's or O's: ")
play_2_name = input('\nWhat is your name player 2: ')
play_2_choice = input("\nAre you X's or O's: ")
user_1 = Player(play_1_name,play_1_choice)
user_1.choose_player()
user_2 = Player(play_2_name,play_2_choice)
user_2.choose_player()
print(f"Let's Play Tic Tac Toe {user_1.name} and {user_2.name}!")
game_1 = Game()
game_1.run()