from commands import parse_command


def test_go_command() -> None:
    assert parse_command("go north") == ("go", "north")


def test_go_command_normalizes_input() -> None:
    assert parse_command(" GO North ") == ("go", "north")


def test_look_command() -> None:
    assert parse_command("look") == ("look", None)


def test_help_command() -> None:
    assert parse_command("help") == ("help", None)


def test_quit_command() -> None:
    assert parse_command("quit") == ("quit", None)


def test_inventory_command() -> None:
    assert parse_command("inventory") == ("inventory", None)


def test_invalid_command() -> None:
    assert parse_command("abc") == ("invalid", None)


def test_empty_input() -> None:
    assert parse_command("") == ("invalid", None)


def test_incomplete_go_command() -> None:
    assert parse_command("go") == ("invalid", None)
