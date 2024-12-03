import sys
from game import Game
from map_editor import MapEditor

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 index.py [game|editor]")
        return

    if sys.argv[1] == "game":
        game = Game()
        game.start_game()
    elif sys.argv[1] == "editor":
        editor = MapEditor()
        editor.start_editor()
    else:
        print("Invalid argument. Use 'game' or 'editor'.")


if __name__ == "__main__":
    main()
