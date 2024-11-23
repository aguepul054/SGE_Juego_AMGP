from First_screen import *

first_screen = First_Screen()

if __name__ == "__main__":
    result = first_screen.tit_screen()
    if result == "start":
        first_screen.go_game()
    elif result == "quit":
        first_screen.go_exit()
