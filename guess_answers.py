questions = [
    {
        "question": "Which keyword define a function?",
        "option": ["A: class", "B: def", "C: loop"],
        "answer": "b"
    },
    {
        "question": "Which data type store true or false?",
        "option": ["A: str", "B: bool", "C: list"],
        "answer": "b"
    },
    {
        "question": "What is 2+2?",
        "option": ["A: 4", "B: 7", "C: 6"],
        "answer": "a"
    }
]

score = 0

for question in questions:
    print(question["question"])

    for option in question["option"]:
        print(option)

    while True:
        ans = input("Enter your answer (a/b/c): ").strip().lower()

        if ans in ["a", "b", "c"]:
            break
        else:
            print("Invalid input! Enter only a, b, or c.")

    if ans == question["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

total = len(questions)
percentage = (score / total) * 100

print("\n=== Quiz Result ===")
print(f"Your score: {score}/{total}")
print(f"Percentage: {percentage:.0f}%")

if percentage == 100:
    print("Excellent work!")
