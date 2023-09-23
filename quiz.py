from question import question 
question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n", 
    "what color are Bannana?\n(a)Teal\n(b)) Magenta\n(c) Yellow\n\n"
    "What color are strawberries?\n(a) Yellow\n(b) Red\n (c) Blue\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0  
    for question in questions: 
        answer = input(questions.prompt)
        if answer == question.answer:
            score += 1 
print("You got " +str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)