
# 🎮 Quiz Battle

**Quiz Battle** is a Python-based command-line quiz game where two players take turns answering questions. At the end, scores are tallied and a winner is declared.

## 📋 Project Structure
```
.
├── main.py           # Entry point, manages game flow
├── quiz_data.py      # Question bank with questions and answers
├── utils.py          # Utility functions for asking questions and saving scores
├── score_log.txt     # Log of previous game scores
```

## 🚀 Features
- Supports two-player gameplay.
- Customizable number of questions per session (default is 5).
- Randomly selects questions from the bank, with immediate feedback on answers.
- Displays final scores and announces the winner.
- Automatically saves the game result to `score_log.txt`.

## 📦 Installation & Running
1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
2️⃣ Run the game:
```bash
python main.py
```
Or specify the number of questions (e.g., 10):
```bash
python main.py 10
```

## 📝 Sample Questions
From `quiz_data.py`:
- What is the capital of France?
- What is 5 + 7?
- Who wrote 'Hamlet'?
- ...

## 🏆 Score History
View `score_log.txt` to see each game's scores and the winner.

## 🤝 Contributions
Feel free to submit issues or pull requests to improve the question bank or enhance the game’s features.
