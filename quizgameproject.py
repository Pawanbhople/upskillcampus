class Question:

  def __init__(self, prompt, options, correct_ans):
    self.prompt = prompt
    self.options = options
    self.correct_ans = correct_ans


class Quiz:

  def __init__(self, questions):
    self.questions = questions
    self.score = 0

  def run_quiz(self):
    for question in self.questions:
      print(question.prompt)
      for i, option in enumerate(question.options):
        print(f"{i + 1}. {option}")
      user_ans = int(input("Enter your choice (1-4): ")) - 1
      if user_ans == question.correct_ans:
        print("Correct answer! +2 Marks")
        self.score += 2
      else:
        print("Wrong answer! -1 Mark")
        self.score -= 1
    print(f"Your final score is {self.score} out of {len(self.questions)*2}.")


# Sample questions
questions = [
    Question("A. What is the capital of Maharashtra ?",
             ["Pune", "Mumbai", "New Delhi", "Nagpur"], 1),
    Question("B. Which is the biggest black holes in our Milky Way galaxy ?",
             ["Sagittarius A*", "Gaia BH1", "TON 618", "Cygnus X-3"], 0),
    Question("C. Who wrote 'Srimad Bhagavad Gita' ?", [
        "Rishi Vishvamitra", "Maharishi Veda Vyasa", "Rishi Kashyap",
        "Maharishi Valmiki"
    ], 1),
    Question("D. What is the GDP of India as per 2023 data ?", [
        "$340.64 billion nominal and $1.57 trillion PPP",
        "$27.97 trillion nominal and $27.97 trillion PPP",
        "$2.186 trillion nominal and $3.193 trillion PPP",
        "$3.732 trillion nominal and $13.119 trillion PPP"
    ], 3),
    Question("E. Who painted the Mona Lisa ?", [
        "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh",
        "Claude Monet"
    ], 0),
    Question("F. What is the chemical symbol for Vinegar?",
             ["NaNO3", "C3H5O3", "CH3COOH", "HCL"], 2),
    Question(
        "G. For the DNA stand 5'-TACGATCATAT-3' the correct complementry DNA stand is ?",
        [
            "3'-TACGATCATAT-5'", "5'-ATGCTAGTATA-3'", "3'-ATGCTAGTATA-5'",
            "3'-TATACTAGCAT-5'"
        ], 2),
    Question(
        "H. What should be the next number in below series ? 3,8,15,24,35......",
        ["44", "47", "48", "49"], 2),
    Question(
        "I. Which of the following is a correct way to declare a Python list ?",
        ["list={1,2,3}", "list=(1,2,3)", "list=1,2,3", "list=[1,2,3]"], 3),
    Question("J. Who is known as the Father of Indian Navy ?", [
        "Chhatrapati Shivaji Maharaj", "Subroto Mukherjee",
        "Major-General Stringer Lawrence", "Mohandas Karamchand Gandhi"
    ], 0)
]

# Create and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
