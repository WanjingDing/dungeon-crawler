# Dungeon Crawler: Prison Escape
# Authors: Wanjing Ding, Kaiyue Lou

## Overview
This project is a text-based dungeon-crawling game implemented in Python.
The player is trapped in a prison maze and must navigate through interconnected rooms, collect a key, and unlock the exit gate to escape.

The project is designed as a modular Python library, where the core game logic is separated from any user interface. A command-line interface (CLI) can be built on top of this logic.

## Game Objective
- Explore the prison maze
- Find the key located in the Evidence Locker
- Avoid the Guard Post, which will send you back to the start
- Reach the Exit Gate and unlock it to win the game

## Project Structure
final_project
- models.py
- engine.py
- commands.py
- cli.py
- tests/ # Unit tests
1. test_engine.py
2. test_commands.py
3. onftest.py
- .github/workflows/ 
- requirements.txt
- pyproject.toml
- README.md
- AI_USAGE.md

## Available Commands
Players can interact with the game using the following commands:
1. go <direction>
Move in a direction (north, south, east, west)
2. look
Display the current room description
3. inventory
Show items the player is carrying
4. help
Show available commands
5. quit
Exit the game

## How to Run the Project
1. Clone the repository
git clone https://github.com/WanjingDing/dungeon-crawler.git
cd dungeon-crawler

2. Set up environment
python -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

## Running Tests
To run all tests:
```bash
pytest
```

Tests cover:
valid and invalid movement
key pickup
guard reset behavior
exit conditions (with and without key)

## Running the game
```bash
python cli.py
```

## Map of the game
                Solitary Wing  -- Evidence Locker (key)
                        |
Intake Cell -- Central Corridor -- Guard Passage -- Guard Post
                        |                |
                    Laundry Cell --   Mess Hall
                                         |
                                    Tunnel Junction --  Exit Gate


## Local testing instructions
Contributors should run tests locally before pushing changes.
Run the test suite with:
```bash
pytest
```

Run linting with:
```bash
ruff check .
```

If needed, you can also format the code with:
```bash
ruff format .
```
These checks help ensure that the code passes local quality control before submission.
