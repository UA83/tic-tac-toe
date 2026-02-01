# Tic-Tac-Toe

A modern, dark-themed Tic-Tac-Toe game implemented in Python using Tkinter.
Features include a sleek UI, score tracking, and auto-reset functionality.

## Prerequisites

- Python 3
- `tkinter` (usually installed with Python, but requires `python3-tk` on some Linux distributions)

## specific Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd tic-tac-toe
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment**:
    - On Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies**:
    There are no external PyPI dependencies, but ensure you have Tkinter installed.
    On Debian/Ubuntu based systems:
    ```bash
    sudo apt-get install python3-tk
    ```

## Running the Game

With the virtual environment activated, run:

```bash
python3 tic_tac_toe.py
```

## How to Play

- The game starts with player 'X'.
- Click on any empty grid cell to place your mark.
- The game alternates turns between 'X' and 'O'.
- The first player to get 3 marks in a row (horizontal, vertical, or diagonal) wins.
- If the grid is full and no one has won, it's a draw.
- Click "Reset Game" to start over.
