from commands import parse_command


def test_go_command():
    assert parse_command("go north") == ("go", "north")


def test_look_command():
    assert parse_command("look") == ("look", None)


def test_invalid_command():
    assert parse_command("abc") == ("invalid", None)


def test_empty_input():
    assert parse_command("") == ("invalid", None)