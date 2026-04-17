from dataclasses import dataclass, field


@dataclass
class Room:
    """Represents a room in the prison maze."""

    name: str
    description: str
    exits: dict[str, str] = field(default_factory=dict)
    locked: bool = False
    has_guard: bool = False
    has_key: bool = False
    is_exit: bool = False
    is_reset: bool = False


@dataclass
class Player:
    """Represents the player in the prison maze."""

    current_room: str
    inventory: list[str] = field(default_factory=list)
