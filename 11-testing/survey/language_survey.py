# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

from survey import AnonymousSurvey


def main():
    # Определение вопроса с созданием экземпляра AnonymousSurvey.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    
    # Вывод вопроса и сохранение ответов.
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
        
    # Вывод результатов опроса.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()


if __name__ == '__main__':
    main()
