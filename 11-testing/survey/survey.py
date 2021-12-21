# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------


class AnonymousSurvey:
    """Сбор анонимных ответов на опросы."""
    
    def __init__(self, question: str):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses: list = []
    
    def show_question(self):
        """Выводит вопрос."""
        print(self.question)
    
    def store_response(self, new_response: str):
        """Сохраняет один ответ на опрос."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


def main():
    pass


if __name__ == '__main__':
    main()
