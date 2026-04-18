from commands import parse_command
from engine import START_ROOM, build_map, move_player
from models import Player


def print_help() -> None:
    """Print available commands."""
    print("Available commands:")
    print("  go north")
    print("  go south")
    print("  go east")
    print("  go west")
    print("  look")
    print("  inventory")
    print("  help")
    print("  quit")


def main() -> None:
    """Run the command-line interface for the game."""
    rooms = build_map()
    player = Player(current_room=START_ROOM)

    print("Welcome to Dungeon Crawler: Prison Escape!")
    print("Type 'help' to see available commands.\n")
    print(rooms[player.current_room].description)

    while True:
        user_input = input("\n> ")
        command, argument = parse_command(user_input)

        if command == "invalid":
            print("Invalid command. Type 'help' to see available commands.")
            continue

        if command == "help":
            print_help()
            continue

        if command == "quit":
            print("Goodbye!")
            break

        if command == "look":
            print(rooms[player.current_room].description)
            continue

        if command == "inventory":
            if player.inventory:
                print("Inventory:", ", ".join(player.inventory))
            else:
                print("Your inventory is empty.")
            continue

        if command == "go":
            if argument is None:
                print("Invalid command. Type 'help' to see available commands.")
                continue

            result = move_player(player, rooms, argument)
            print(result)

            if "You win!" in result:
                print("Game over.")
                break


if __name__ == "__main__":
    main()
