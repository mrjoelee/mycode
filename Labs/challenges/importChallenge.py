#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com

Module Import Challenge """
import html

def main():


    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }

    question = html.unescape(trivia["question"])
    correct = html.unescape(trivia["correct_answer"])
    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    incorrect3 = html.unescape(trivia["incorrect_answers"][2])

    print(f"question: {question}")
    print(f"correct: {correct}")
    print(f"incorrect1: {incorrect1}")
    print(f"incorrect2: {incorrect2}")
    print(f"incorrect3: {incorrect3}")

if __name__ == "__main__":
    main()
