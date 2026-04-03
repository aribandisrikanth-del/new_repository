import random

class fruit_quiz():
    def __init__(self):
        self.fruits={"apple":"red","orange":"orane","banana":"yellow","guava":"green",}
    def quiz(self):
        while(True):
            fruit, color=random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option=int(input("enter 0 if you want to try again, otherwise enter 1 "))
            if (option):
                break
print("welcome to fruit quiz")
fq=fruit_quiz()
fq.quiz()