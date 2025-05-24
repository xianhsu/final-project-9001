import random
from quiz_data import questions # type: ignore

def ask_question(player_name):
    question = random.choice(questions)
    answer = input(f"{player_name}, {question['question']} ").strip().lower()
    if answer == question["answer"]:
        print("Correct! ✅")
        return True
    else:
        print(f"Wrong! ❌ The correct answer was: {question['answer']}")
        return False

def save_score(p1, p2, scores):
    with open("score_log.txt", "a") as f:
        f.write(f"Game Result\n")
        f.write(f"{p1}: {scores[p1]} points\n")
        f.write(f"{p2}: {scores[p2]} points\n")
        f.write(f"Winner: {max(scores, key=scores.get)}\n")
        f.write("-" * 30 + "\n")
