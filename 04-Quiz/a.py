answer = ["c++", "python", "javascript"]
questions = ["which language is the fastest?", "which language is the most used?", "which language is the most versatile?"]
restart = True

print("welcome to my quizz")
    
def question(question, answer):
        
        print(question)
        choice = input("your answer: ")
        for i in range(2):
            if choice.lower().strip() == answer:
                break
            else:
                print("wrong answer, try again")
                choice = input("your answer: ")
        if choice.lower().strip() != answer:
            print("wrong answer") 
            return 0
        print("correct")
        return 1
while restart:
    score = 0
    
    for i in range(len(questions)):
        score += question(questions[i], answer[i])
        print(f"your score is: {score}/{len(questions)}")

    moyenne_score = score / len(questions) * 100
    print(f"your average score is: {moyenne_score:.2f}")


    print("wanna play again? y/n")
    again = input()
    if again.lower() == "y":
     restart = True
    else : 
        restart = False
