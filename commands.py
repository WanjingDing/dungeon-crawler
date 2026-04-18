def parse_command(user_input: str) -> tuple[str, str | None]:
    text = user_input.strip().lower()

    if not text:
        return ("invalid", None)

    parts = text.split()

    if parts[0] == "go":
        if len(parts) != 2:
            return ("invalid", None)
        return ("go", parts[1])

    if parts[0] in {"look", "help", "quit", "inventory"}:
        if len(parts) != 1:
            return ("invalid", None)
        return (parts[0], None)

    return ("invalid", None)