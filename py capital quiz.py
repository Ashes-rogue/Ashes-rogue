import time
import random

class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of Afghanistan?", "answer": "Kabul"},
            {"question": "What is the capital of Australia?", "answer": "Canberra"},
            {"question": "What is the capital of Brazil?", "answer": "Brasilia"},
            {"question": "What is the capital of Canada?", "answer": "Ottawa"},
            {"question": "What is the capital of China?", "answer": "Beijing"},
            {"question": "What is the capital of Egypt?", "answer": "Cairo"},
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is the capital of Germany?", "answer": "Berlin"},
            {"question": "What is the capital of India?", "answer": "New Delhi"},
            {"question": "What is the capital of Italy?", "answer": "Rome"},
            {"question": "What is the capital of Japan?", "answer": "Tokyo"},
            {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
            {"question": "What is the capital of Russia?", "answer": "Moscow"},
            {"question": "What is the capital of South Africa?", "answer": "Cape Town"},
            {"question": "What is the capital of Spain?", "answer": "Madrid"},
            {"question": "What is the capital of the United Kingdom?", "answer": "London"},
            {"question": "What is the capital of the United States?", "answer": "Washington, D.C."},
            {"question": "What is the capital of Malaysia?", "answer": "Kuala Lumpur"},
            {"question": "What is the capital of Singapore?", "answer": "Singapore"},
            {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
            {"question": "What is the capital of Austria?", "answer": "Vienna"},
            {"question": "What is the capital of South Korea?", "answer": "Seoul"},
            {"question": "What is the capital of Turkey?", "answer": "Ankara"},
            {"question": "What is the capital of Belgium?", "answer": "Brussels"},
            {"question": "What is the capital of Chile?", "answer": "Santiago"},
            {"question": "What is the capital of Denmark?", "answer": "Copenhagen"},
            {"question": "What is the capital of Finland?" ,"answer": "Helsinki"},
            {"question": "What is the capital of Iran?", "answer": "Tehran"},
            {"question": "What is the capital of Iraq?", "answer": "Baghdad"},
            {"question": "What is the capital of Ireland?", "answer": "Dublin"},
            {"question": "What is the capital of Greece?", "answer": "Athens"},
            {"question": "What is the capital of Netherlands?", "answer": "Amsterdam"},
            {"question": "What is the capital of Indonesia?", "answer": "Jakarta"},
            {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
            {"question": "What is the capital of Poland?", "answer": "Warsaw"},
            {"question": "What is the capital of Pakistan?", "answer": "Islamabad"},
            {"question": "What is the capital of Norway?", "answer": "Oslo"},
            {"question": "What is the capital of Philippines?", "answer": "Manila"},
            {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
            {"question": "What is the capital of Vietnam?", "answer": "Hanoi"},
            {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
            {"question": "What is the capital of Switzerland?", "answer": "Bern"},
            {"question": "What is the capital of Bahrain?", "answer": "Manama"},
            {"question": "What is the capital of Bhutan?", "answer": "Thimphu"},
            {"question": "What is the capital of Cambodia?", "answer": "Phnom Penh"},
            {"question": "What is the capital of Ecuador?", "answer": "Quito"},
            {"question": "What is the capital of Fiji?", "answer": "Suva"},
            {"question": "What is the capital of Maldives?", "answer": "Male"},
            {"question": "What is the capital of Hungary?", "answer": "Budapest"},
            {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
            {"question": "What is the capital of Jordan?", "answer": "Amman"},
            {"question": "What is the capital of Kenya?", "answer": "Nairobi"},
            {"question": "What is the capital of Kuwait?", "answer": "Kuwait City"},
            {"question": "What is the capital of Libya?", "answer": "Tripoli"},
            {"question": "What is the capital of Luxembourg?", "answer": "Luxembourg City"},
            {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
            {"question": "What is the capital of Monaco?", "answer": "Monaco"},
            {"question": "What is the capital of Oman?", "answer": "Muscat"},
            {"question": "What is the capital of Peru?", "answer": "Lima"},
            {"question": "What is the capital of Seychelles?", "answer": "Victoria"},
            {"question": "What is the capital of Uganda?", "answer": "Kampala"},
            {"question": "What is the capital of Zimbabwe?", "answer": "Harare"},
        ]
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        user_answer = input("Your answer: ").strip().lower()
        self.check_answer(user_answer, question["answer"])

    def check_answer(self, user_answer, correct_answer):
        if isinstance(correct_answer, list):
            correct_answer = [ans.lower() for ans in correct_answer]
        else:
            correct_answer = correct_answer.lower()
        if user_answer in correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry, the correct answer is: {', '.join(correct_answer) if isinstance(correct_answer, list) else correct_answer}.")

    def run_quiz(self):
        while True:
            print("Welcome to the Country Capital Quiz!")
            num_rounds = int(input("How many rounds would you like to play? "))
            random.shuffle(self.questions)
            selected_questions = self.questions[:num_rounds]

            start_time = time.time()
            
            self.score = 0

            for question in selected_questions:
                self.display_question(question)
            
            end_time = time.time()
            time_taken = end_time - start_time

            print(f"Quiz completed! Your final score is {self.score}/{num_rounds}")
            print(f"Time taken: {time_taken:.2f} seconds")

            if not self.play_again():
                print("Thank you for playing! Goodbye!")
                break

    def play_again(self):
        again = input("Would you like to play again? (yes/no): ").strip().lower()
        if again in ['yes', 'y']:
            return True
        elif again in ['no', 'n']:
            return False
        else:
            print("Invalid response.")
            return self.play_again()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
