# Dungeon Crawler: Prison Escape
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
final_project/
├── models.py
├── engine.py
├── tests/ # Unit tests
│ └── test_engine.py
├── .github/workflows/ 
├── requirements.txt
├── pyproject.toml
└── README.md

## How to Run the Project
1. Clone the repository
git clone <your-repo-link>
cd final_project

2. Set up environment
python -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

## Running Tests
To run all tests:
pytest

Tests cover:
valid and invalid movement
key pickup
guard reset behavior
exit conditions (with and without key)