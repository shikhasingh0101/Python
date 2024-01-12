class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self, user):
        user_score = 0

        print(f"Welcome to the {self.quiz_name} Quiz!")

        for index, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {question.question_text}")
            user_answer = input("Your answer: ")

            if question.check_answer(user_answer):
                print("Correct!")
                user_score += 1
            else:
                print(f"Wrong! The correct answer is: {question.correct_answer}")

        print(f"\nQuiz Completed! Your score: {user_score}/{len(self.questions)}")
        user.set_score(self.quiz_name, user_score)

class User:
    def __init__(self, username):
        self.username = username
        self.scores = {}

    def set_score(self, quiz_name, score):
        self.scores[quiz_name] = score

    def display_scores(self):
        print(f"\n{self.username}'s Quiz Scores:")
        for quiz_name, score in self.scores.items():
            print(f"{quiz_name}: {score}/{len(quizzes[quiz_name].questions)}")

# Example usage:
# Create questions
question1 = Question("What is the capital of France?", "Paris")
question2 = Question("What is the largest planet in our solar system?", "Jupiter")
question3 = Question("Which programming language is known as the 'language of the web'?", "JavaScript")

# Create a quiz and add questions
quiz1 = Quiz("General Knowledge Quiz")
quiz1.add_question(question1)
quiz1.add_question(question2)

quiz2 = Quiz("Programming Quiz")
quiz2.add_question(question3)

# Create a user
user1 = User("Alice")

# Take quizzes
quizzes = {"General Knowledge Quiz": quiz1, "Programming Quiz": quiz2}
quiz1.take_quiz(user1)
quiz2.take_quiz(user1)

# Display user scores
user1.display_scores()
