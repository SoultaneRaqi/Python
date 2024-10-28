
def run_quiz(questions, test_mode=False):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        
        # Use a hardcoded answer if test_mode is True; otherwise, ask for input
        answer = "A" if test_mode else input("Enter your answer (A, B, C, or D): ").upper()
        
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")


# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital city of Morocco?",
        "options": ["A. Rabat", "B. Casablanca", "C. Marrakech", "D.Fes"],
        "answer": "A"
    },
    {
        "prompt": "What is the currency used in Morocco?",
        "options": ["A. Riyal", "B. Dirham", "C. Dinar", "D. Dollar"],
        "answer": "B"
    },
    {
        "prompt": "Which Moroccan city is famous for its blue-painted streets?",
        "options": ["A. Agadir", "B. Tangier", "C. Chefchaouen", "D. Rabat"],
        "answer": "C"
    },
     {
        "prompt": "Which mountain range runs through Morocco?",
        "options": ["A. Andes", "B. Rockies", "C. Atlas Mountains", "D. Pyrenees"],
        "answer": "C"
    },
    {
        "prompt": "What is the name of the traditional Moroccan stew cooked in a conical pot?",
        "options": ["A. Couscous", "B. Tajine", "C. Shawarma", "D. Paella"],
        "answer": "B"
    },
    {
        "prompt": "Which Moroccan city is known as the 'Red City'?",
        "options": ["A. Fes", "B. Casablanca", "C. Marrakech", "D. Tangier"],
        "answer": "C"
    },
    {
        "prompt": "What is the main religion practiced in Morocco?",
        "options": ["A. Christianity", "B. Islam", "C. Hinduism", "D. Buddhism"],
        "answer": "B"
    },
    {
        "prompt": "Which desert covers a large part of southeastern Morocco?",
        "options": ["A. Gobi", "B. Mojave", "C. Sahara", "D. Sonoran"],
        "answer": "C"
    },
    {
        "prompt": "What is the name of the Moroccan festival that celebrates the harvest of roses?",
        "options": ["A. Rose Harvest Festival", "B. Rose Garden Festival", "C. Festival of Roses", "D. Rose Celebration"],
        "answer": "C"
    },
   
]

# Run the quiz
run_quiz(questions)