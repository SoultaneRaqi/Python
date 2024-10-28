def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
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
    {
        "prompt": "Morocco gained independence from which country in 1956?",
        "options": ["A. Spain", "B. Portugal", "C. France", "D. Italy"],
        "answer": "C"
    },
     {
        "prompt": "What is the largest city in Morocco?",
        "options": ["A. Casablanca", "B. Rabat", "C. Marrakech", "D. Fes"],
        "answer": "A"
    },
    {
        "prompt": "What is the name of the strait that separates Morocco from Spain?",
        "options": ["A. Strait of Gibraltar", "B. Bosphorus Strait", "C. Magellan Strait", "D. Malacca Strait"],
        "answer": "A"
    },
    {
        "prompt": "Which famous Moroccan city is known as the 'Gateway to the Sahara'?",
        "options": ["A. Tangier", "B. Essaouira", "C. Ouarzazate", "D. Agadir"],
        "answer": "C"
    },
    {
        "prompt": "What color is traditionally associated with Moroccan architecture and interiors?",
        "options": ["A. Blue", "B. White", "C. Green", "D. Red"],
        "answer": "A"
    },
    {
        "prompt": "Which Mediterranean dish is a staple in Moroccan cuisine?",
        "options": ["A. Paella", "B. Falafel", "C. Couscous", "D. Pasta"],
        "answer": "C"
    },
    {
        "prompt": "Which Moroccan city is known for its annual film festival?",
        "options": ["A. Casablanca", "B. Marrakech", "C. Tangier", "D. Fes"],
        "answer": "B"
    },
    {
        "prompt": "What is the name of the Moroccan king who began his reign in 1999?",
        "options": ["A. King Mohammed VI", "B. King Hassan II", "C. King Abdullah", "D. King Saud"],
        "answer": "A"
    },
    {
        "prompt": "Which Moroccan landmark is one of the largest mosques in the world?",
        "options": ["A. Koutoubia Mosque", "B. Hassan II Mosque", "C. Al-Qarawiyyin Mosque", "D. Tinmel Mosque"],
        "answer": "B"
    },
    {
        "prompt": "In which city is the famous Jemaa el-Fnaa square located?",
        "options": ["A. Rabat", "B. Casablanca", "C. Marrakech", "D. Fes"],
        "answer": "C"
    },
    {
        "prompt": "What is the traditional Moroccan mint tea called?",
        "options": ["A. Chai", "B. Atay", "C. Karak", "D. Moroccan Tea"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(questions)
