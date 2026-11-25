# Case Study 31: String-Based Examination Answer Evaluation
answer_key = ["A", "C", "B", "D", "A"]
answers = []

for i in range(5):
    answer = input(f"Enter answer for question {i + 1} (A/B/C/D or Enter to skip): ")
    answers.append(answer.strip().upper())

correct = 0
incorrect = 0
unanswered = 0

for i in range(5):
    if answers[i] == "":
        unanswered += 1
    elif answers[i] == answer_key[i]:
        correct += 1
    else:
        incorrect += 1

print(f"Correct answers: {correct}")
print(f"Incorrect answers: {incorrect}")
print(f"Unanswered questions: {unanswered}")
print(f"Final score: {correct}/5")
