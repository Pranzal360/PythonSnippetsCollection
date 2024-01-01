# a dictionary that stores questions and asnwer
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pair 
# display each question to the user and allow them to answer 
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "Question1" : {
        "question" : "What is the capital of france?",
        "answer": "Paris"
    },
    "question2" : {
        "question" : "What is the capital of germeny",
        "answer": "Berlin"
    },
    "question3": {
        "question" : "What is the capital of Itly ?",
        "answer" : "Rome"
    },
    "Question4" : {
        "question" : "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "questio5" : {
        "question" : "What is the capital of Portugal",
        "answer": "Lisbon"
    },
    "question6": {
        "question" : "What is the capital of Swtitzerland ?",
        "answer" : "Bern"
    },
    "question7": {
        "question" : "What is the capital of Austria ?",
        "answer" : "vienna"
    },
}

score = 0

for key,value in quiz.items():
    print(f"\n {value['question']}")
    answer = input("Answer: ")

    if answer.lower() == value["answer"].lower():
        print("correct")
        score +=1
        print(f"your score is {score}")
    
    else:
        print("incorrect")
        print(f" the answer is {value['answer']} \n")

print(f"you got {int((score / 7)* 0.1)}%")