from engine import KEY_ITEM, START_ROOM, build_map, move_player
from models import Player


def test_move_player_to_connected_room() -> None:
    rooms = build_map()
    player = Player(current_room=START_ROOM)

    result = move_player(player, rooms, "east")

    assert player.current_room == "Central Corridor"
    assert result == rooms["Central Corridor"].description


def test_move_player_invalid_direction() -> None:
    rooms = build_map()
    player = Player(current_room=START_ROOM)

    result = move_player(player, rooms, "north")

    assert player.current_room == START_ROOM
    assert result == "You can't go that way."


def test_guard_post_resets_player_to_start() -> None:
    rooms = build_map()
    player = Player(current_room="Guard Passage")

    result = move_player(player, rooms, "east")

    assert player.current_room == START_ROOM
    assert "A guard caught you" in result


def test_collect_key_in_evidence_locker() -> None:
    rooms = build_map()
    player = Player(current_room="Solitary Wing")

    result = move_player(player, rooms, "east")

    assert player.current_room == "Evidence Locker"
    assert KEY_ITEM in player.inventory
    assert "You found the key!" in result


def test_cannot_win_without_key() -> None:
    rooms = build_map()
    player = Player(current_room="Tunnel Junction")

    result = move_player(player, rooms, "east")

    assert player.current_room == "Exit Gate"
    assert "You need the key" in result


def test_win_with_key() -> None:
    rooms = build_map()
    player = Player(current_room="Tunnel Junction", inventory=[KEY_ITEM])

    result = move_player(player, rooms, "east")

    assert player.current_room == "Exit Gate"
    assert "You win!" in result
