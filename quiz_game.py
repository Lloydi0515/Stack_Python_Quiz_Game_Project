
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    

question_prompts = [
    "Is the coding language Python, named after a snake?\n(A) No\n(B) Yes\n(C) Person\n(D) Both A & B\n\n",
    "What Does CPU stand for?\n(A) Center Processing Unit\n(B) Central Processing Unit\n(C) Central Processing Unix\n(D) Center Process Unit\n\n",
    "What Does GPU stand for?\n(A) Graphical Processing Unit\n(B) Graphics Processing Unit\n(C) Game Process Unit\n(D) Graphics Process Unit\n\n",
    "What Does RAM stand for?\n(A)Rand Access Memory\n(B)Random Access Memo\n(C) Reverse Access Memory\n(D) Random Access Memory\n\n",
    "Who Invented the first computer?\n(A) Steve Jobs\n(B) Bill Gates\n(C) Charles Babbage\n(D) Alexander Graham Bell\n\n"
]
# User question
questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "B"),
    Question(question_prompts[3], "D"),
    Question(question_prompts[4], "C")

]

# function that run the test, check they got answer right

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        answer = answer.upper()
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)













