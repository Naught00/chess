from display import *
from game import singleplayer


def main():
    selection = main_menu()
    match selection:
        case '1':
            singleplayer()

main()
# player 2
# knights
# show board func
# multiplayer
