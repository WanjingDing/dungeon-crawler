from engine import START_ROOM, build_map, move_player
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
    assert rooms[START_ROOM].description in result
