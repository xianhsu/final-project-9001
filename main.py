import sys
from quiz_data import questions # type: ignore
from utils import ask_question, save_score # type: ignore

def main():
    if len(sys.argv) > 1:
        total_questions = int(sys.argv[1])
    else:
        total_questions = 5

    print("=== Welcome to Quiz Battle ===")
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    players = [player1, player2]
    scores = {player1: 0, player2: 0}
    turn = 0

    for i in range(total_questions):
        current_player = players[turn % 2]
        print(f"\n--- Question {i + 1} ---")
        if ask_question(current_player):
            scores[current_player] += 1
        turn += 1

    print("\n=== Final Scores ===")
    for p in players:
        print(f"{p}: {scores[p]} points")

    winner = max(scores, key=scores.get)
    print(f"\n🎉 {winner} wins! 🎉")

    save_score(player1, player2, scores)

if __name__ == "__main__":
    main()
