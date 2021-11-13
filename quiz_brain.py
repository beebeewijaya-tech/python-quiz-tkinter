class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = f"Q.{self.question_number}: {self.current_question.text} (True/False): "
        return question

    def check_answer(self, answer):
        correct_answer = self.current_question.answer
        is_true = answer.lower() == correct_answer.lower()
        if is_true:
            self.score += 1
        else:
            self.score += 0

        return is_true

