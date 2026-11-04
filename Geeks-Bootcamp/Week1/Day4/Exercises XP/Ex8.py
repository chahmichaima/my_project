data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def run_quiz():
    correct_count = 0
    incorrect_count = 0
    wrong_answers_list = []

    for item in data:
        user_answer = input(item["question"] + " : ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct_count += 1
            print("Correct !\n")
        else:
            incorrect_count += 1
            print(f"Incorrect. La bonne réponse était : {item['answer']}\n")
            wrong_answers_list.append({
                "question": item["question"],
                "user_answer": user_answer,
                "correct_answer": item["answer"]
            })
    return correct_count, incorrect_count, wrong_answers_list
def show_results(correct, incorrect):
    print("--- Résultat du Quiz ---")
    print(f"Nombre de réponses correctes : {correct}")
    print(f"Nombre de réponses incorrectes : {incorrect}\n")
