# 🎮 CODSOFT Task 2: Tic-Tac-Toe AI

A simple **Tic-Tac-Toe game with Artificial Intelligence (AI)** built using **Python**.

In this project, the player plays against an AI opponent. The AI uses the **Minimax Algorithm** to make the best possible moves.

This project was developed as part of the **CODSOFT Python Programming Internship – Task 2**.

## 📌 Features

* 🎮 Player vs AI gameplay
* ❌ Player uses **X**
* ⭕ AI uses **O**
* 🧠 AI uses the **Minimax Algorithm**
* 🏆 Automatically detects the winner
* 🤝 Detects draw situations
* ⚠️ Validates player input
* 🔄 Prevents selecting an already occupied position
* 💻 Runs in the command line/terminal

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Lists
* Loops
* Conditional statements
* Exception handling
* Recursion
* **Minimax Algorithm**

## 📂 Project Structure

```text
tic-tac-toe-ai/
│
├── tic_tac_toe.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
```

### 2. Open the Project Folder

```bash
cd tic-tac-toe-ai
```

### 3. Run the Program

```bash
python tic_tac_toe.py
```

## 🎯 How to Play

The game board contains **9 positions**:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Enter a number from **1 to 9** to place your `X`.

For example:

```text
Enter position (1-9): 5
```

The AI will then automatically select the best available position.

## 🧠 Minimax Algorithm

The AI uses the **Minimax Algorithm** to decide its moves.

The algorithm evaluates possible future game states and chooses the move that gives the AI the best outcome.

### Score System

| Result      | Score |
| ----------- | ----: |
| AI wins     |  `+1` |
| Player wins |  `-1` |
| Draw        |   `0` |

The AI tries to **maximize its score**, while assuming that the player will try to **minimize the AI's score**.

### Basic Working

```text
              Current Game
                    |
              Possible Moves
                    |
              Minimax Search
                    |
        ┌───────────┴───────────┐
        ↓                       ↓
     AI Move                 Player Move
        ↓                       ↓
       Best                   Best
      Score                  Counter
        └───────────┬───────────┘
                    ↓
              AI chooses
              best move
```

## 💻 Example Output

```text
TIC-TAC-TOE
You are X
AI is O

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Enter position (1-9): 1

X |   |  
--+---+--
  | O |  
--+---+--
  |   |  

AI is thinking...

Enter position (1-9): 3
```

If the player wins:

```text
X | X | X
--+---+--
O | O |  
--+---+--
  |   |  

You win!
```

If the AI wins:

```text
O | O | O
--+---+--
X | X |  
--+---+--
  |   |  

AI wins!
```

If there are no available positions:

```text
It's a draw!
```

## 🔍 Important Functions

### `print_board()`

Displays the current Tic-Tac-Toe board.

### `check_winner(player)`

Checks all possible winning combinations.

### `is_full()`

Checks whether all 9 positions are occupied.

### `minimax(is_maximizing)`

Evaluates possible moves recursively and calculates the best score.

### `ai_move()`

Uses the Minimax algorithm to select the best move for the AI.

## 🎓 Learning Objectives

This project helps in understanding:

* Python programming
* Functions
* Lists
* Loops
* Recursion
* Exception handling
* Game logic
* Artificial Intelligence basics
* Decision-making algorithms
* Minimax Algorithm

## 🔮 Future Improvements

The project can be improved by adding:

* 🎨 Graphical User Interface using **Tkinter**
* 👥 Player vs Player mode
* 🎚️ Easy, Medium, and Hard difficulty levels
* 🔊 Sound effects
* 🏆 Scoreboard
* 🔄 Restart game button
* 🌐 Web-based version
* 🤖 More advanced AI strategies

## 👩‍💻 Author

**Prachi**

## 📜 Internship

**CODSOFT Python Programming Internship**

### Task 2 – Tic-Tac-Toe AI

This project was created for educational purposes as part of the CODSOFT internship.

## ⭐ Acknowledgement

Thanks to **CODSOFT** for providing the opportunity to work on Python programming projects and improve practical programming skills.

## 📄 License

This project is created for **educational purposes**.
