def run_quiz():
    geography_questions = [
        {
            "question": "What is the largest continent in the world?",
            "options": ["Africa", "Asia", "Europe", "North America"],
            "answer": "Asia"
        },
    
        {
            "question": "Which is the longest river in the world?",
            "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
            "answer": "Nile River"
        },
    
        {
            "question": "What is the capital of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
            "answer": "Canberra"
        },
    
        {
            "question": "Which is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
            "answer": "Pacific Ocean"
        },
    
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "South Korea", "Thailand"],
            "answer": "Japan"
        },
    
        {
            "question": "Which desert is the largest hot desert in the world?",
            "options": ["Gobi Desert", "Sahara Desert", "Kalahari Desert", "Thar Desert"],
            "answer": "Sahara Desert"
        },
    
        {
            "question": "Mount Everest is located in which mountain range?",
            "options": ["Andes", "Alps", "Himalayas", "Rocky Mountains"],
            "answer": "Himalayas"
        },
    
        {
            "question": "Which country has the largest land area in the world?",
            "options": ["Canada", "China", "Russia", "United States"],
            "answer": "Russia"
        },
    
        {
            "question": "Which Indian state has the longest coastline?",
            "options": ["Maharashtra", "Tamil Nadu", "Gujarat", "Andhra Pradesh"],
            "answer": "Gujarat"
        },
    
        {
            "question": "Which is the smallest continent by land area?",
            "options": ["Europe", "Australia", "Antarctica", "South America"],
            "answer": "Australia"
        }
    ]

    score = 0
    for index, q in enumerate(geography_questions):
        print(f"{index + 1} : {q["question"]}")
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer : ")
        if user_answer == q["answer"]:
            print("Correct Answer! \n")
            score += 1


    print("Your final score is : " , score)

run_quiz()
