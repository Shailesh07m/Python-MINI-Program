question=("How many element in periodic table ?",
          "Which animal lays the largest eggs?",
          "What is most abundunt gas in Earth's Atmosphere?",
          "How many  bones are in Human body?",
          "Which planet in solar system is hottest?",)
options=(("A.116","B.117","C.118","D.119"),
         ("A. Whale","B. Crocodile","C. Elephant","D.Ostrich"),
         ("A. Nitrogen","B. Oxygen","C. carbon - dioxide","D. Hydrogen"),
         ("A.206","B.200","C.150","D.207"),
         ("A.Mercury","B.Venus","C.Earth","D.Mars"))


answer=("C","D","A","A","B")
score=0
guesses=[]
score=0
ques_num=0

for q in  question:
    print("-----------------------------------")
    print(q)
    for o in options[ques_num]:
        print(o)

    guess=input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess== answer[ques_num]:
        score=+1
        print("You guessed correctly")
    else:
        print("You Guessed incorrectly")
        print(f"{answer[ques_num]} is Correct Option")
    ques_num+=1

print("Your score is",score)