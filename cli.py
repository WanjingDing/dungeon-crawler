from commands import parse_command
from engine import START_ROOM, build_map, move_player
from models import Player, Room


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


def describe_current_room(player: Player, rooms: dict[str, Room]) -> str:
    """Return a fuller description of the current room."""
    room = rooms[player.current_room]
    exits = ", ".join(room.exits.keys())

    lines = [room.description, f"Exits: {exits}"]

    if room.has_key:
        lines.append("You notice a key in this room.")

    return "\n".join(lines)


def main() -> None:
    """Run the command-line interface for the game."""
    rooms = build_map()
    player = Player(current_room=START_ROOM)

    print("Welcome to Dungeon Crawler: Prison Escape!")
    print("Type 'help' to see available commands.\n")
    print(describe_current_room(player, rooms))

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
            print(describe_current_room(player, rooms))
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
