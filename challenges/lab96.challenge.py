#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
from string import ascii_lowercase

URL= "https://opentdb.com/api.php?amount=5&category=21"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    questions = requests.get(URL).json()

    #enumrates will start the question with #1
    for num, question in enumerate(questions.get('results'), start=1):
        print(f'\nQuestion {num}:')
        #gets the question from the api
        print(f"{question.get('question')}?")
        #storing incorrect answer
        choice = question.get('incorrect_answers')
        #since choice is a list, appending correct_answer and making 1 whole choice
        choice.append(question.get('correct_answer'))
        #storing correct answer
        correct_answer = question.get('correct_answer')
        #testing purposes
        print(correct_answer)
      #use string.ascii_lowercase to get letters that label choices.
      #combine letters and choices  with zip() and store them in a dictionary
        label_choice = dict(zip(ascii_lowercase, sorted(choice)))
        #looping to create the choices below the questions
        for label, choice in label_choice.items():
          print(f"{label} {choice}")
        #asking for user's choice
        answer_label = input("\nChoice?")
        #storing answer from the user's input
        answer = label_choice.get(answer_label)
        #validation of answer
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect, The answer is {correct_answer}")

if __name__ == "__main__":
    main()
