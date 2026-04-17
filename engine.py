from models import Player, Room

START_ROOM = "Intake Cell"


def build_map() -> dict[str, Room]:
    """Create the prison maze based on the agreed map design."""

    rooms = {
        "Intake Cell": Room(
            name="Intake Cell",
            description=(
                "Your starting point in the prison. "
                "Somewhere in this maze lies the key to your freedom. "
                "Find it and unlock the exit gate. "
                "But beware—the guard is watching, and getting caught will send you back."
            ),
            exits={"east": "Central Corridor"},
        ),
        "Central Corridor": Room(
            name="Central Corridor",
            description=(
                "The central corridor stretches in multiple directions. "
                "You hear distant footsteps echoing through the halls. "
                "This place connects many parts of the prison."
            ),
            exits={
                "west": "Intake Cell",
                "east": "Guard Passage",
                "north": "Solitary Wing",
                "south": "Laundry Cell",
            },
        ),
        "Guard Passage": Room(
            name="Guard Passage",
            description=(
                "A narrow passage frequently patrolled by guards. "
                "The air feels tense, and every step must be taken carefully."
            ),
            exits={
                "west": "Central Corridor",
                "east": "Guard Post",
                "south": "Mess Hall",
            },
        ),
        "Guard Post": Room(
            name="Guard Post",
            description=(
                "You have entered the guard post. A guard is stationed here! "
                "You are caught! You're being sent back to the intake cell..."
            ),
            exits={"west": "Guard Passage"},
            has_guard=True,
            is_reset=True,
        ),
        "Solitary Wing": Room(
            name="Solitary Wing",
            description=(
                "Rows of isolated cells line the walls. "
                "It is quiet here—too quiet. You feel uneasy being alone."
            ),
            exits={"south": "Central Corridor", "east": "Evidence Locker"},
        ),
        "Evidence Locker": Room(
            name="Evidence Locker",
            description=(
                "Shelves of confiscated items fill the room. "
                "Among the clutter, something important catches your eye... "
                "This must be where the key is hidden."
            ),
            exits={"west": "Solitary Wing"},
            has_key=True,
        ),
        "Laundry Cell": Room(
            name="Laundry Cell",
            description=(
                "The sound of machines hums softly. Damp clothes hang everywhere. "
                "It seems like a dead end, but maybe useful for hiding."
            ),
            exits={"north": "Central Corridor"},
        ),
        "Mess Hall": Room(
            name="Mess Hall",
            description=(
                "Long tables and trays are scattered around. "
                "This place was once full of noise, now eerily silent."
            ),
            exits={"north": "Guard Passage", "south": "Tunnel Junction"},
        ),
        "Tunnel Junction": Room(
            name="Tunnel Junction",
            description=(
                "You are in a dim underground tunnel. Paths split here. "
                "A faint breeze suggests an exit nearby."
            ),
            exits={"north": "Mess Hall", "east": "Exit Gate"},
        ),
        "Exit Gate": Room(
            name="Exit Gate",
            description=(
                "A massive reinforced gate blocks your way to freedom. "
                "It is locked—you will need a key to escape."
            ),
            exits={"west": "Tunnel Junction"},
            locked=True,
            is_exit=True,
        ),
    }

    return rooms


def move_player(
    player: Player,
    rooms: dict[str, Room],
    direction: str,
) -> str:
    """Move the player in the given direction if possible."""

    current_room = rooms[player.current_room]

    if direction not in current_room.exits:
        return "You can't go that way."

    next_room_name = current_room.exits[direction]
    next_room = rooms[next_room_name]

    if next_room.is_reset:
        player.current_room = START_ROOM
        start_room = rooms[START_ROOM]
        return (
            "A guard caught you and sent you back to the start.\n"
            f"{start_room.description}"
        )

    player.current_room = next_room_name
    return next_room.description
