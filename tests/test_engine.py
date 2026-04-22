from engine import KEY_ITEM, START_ROOM, build_map, move_player
from models import Player


def test_move_player_to_connected_room() -> None:
    rooms = build_map()
    player = Player(current_room=START_ROOM)

    result = move_player(player, rooms, "east")

    assert player.current_room == "Central Corridor"
    assert isinstance(result, str)


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
    assert "guard" in result.lower()
    assert "caught" in result.lower()


def test_collect_key_in_evidence_locker() -> None:
    rooms = build_map()
    player = Player(current_room="Solitary Wing")

    result = move_player(player, rooms, "east")

    assert player.current_room == "Evidence Locker"
    assert KEY_ITEM in player.inventory
    assert "key" in result.lower()


def test_cannot_win_without_key() -> None:
    rooms = build_map()
    player = Player(current_room="Tunnel Junction")

    result = move_player(player, rooms, "east")

    assert player.current_room == "Exit Gate"
    assert "need the key" in result.lower() or "locked" in result.lower()


def test_win_with_key() -> None:
    rooms = build_map()
    player = Player(current_room="Tunnel Junction", inventory=[KEY_ITEM])

    result = move_player(player, rooms, "east")

    assert player.current_room == "Exit Gate"
    assert "you win!" in result.lower()


def test_guard_post_has_guard() -> None:
    rooms = build_map()
    assert rooms["Guard Post"].has_guard is True


def test_exit_gate_is_locked() -> None:
    rooms = build_map()
    assert rooms["Exit Gate"].locked is True
