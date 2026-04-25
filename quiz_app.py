import tkinter as tk        #importing tkinter module
import random               #for randomizing questions

#---Questions---
#Questions stored in a dictionary
quiz_data = {
    "easy": [
        {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"], "answer": "Delhi"},
        {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "Which language is used for Python?", "options": ["Java", "English", "C++", "Binary"], "answer": "English"}
    ],      #Easy level questions
    "medium": [
        {"question": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
        {"question": "What is len('Python')?", "options": ["5", "6", "7", "Error"], "answer": "6"},
        {"question": "Which keyword defines a function?", "options": ["func", "define", "def", "function"], "answer": "def"}
    ],      #Medium level questions 
    "hard": [
        {"question": "Time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "answer": "O(log n)"},
        {"question": "Which module is used for regex?", "options": ["pyregex", "regex", "re", "pattern"], "answer": "re"},
        {"question": "What does 'self' refer to?", "options": ["Class", "Instance", "Function", "Variable"], "answer": "Instance"}
    ]       #Hard level questions
}

#---Main App---
class QuizApp:
    def __init__(self, root):       #Main window
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("350x300")
        self.root.configure(bg="#000000")

        self.score = 0          #User score
        self.q_index = 0        #Current question index
        self.questions = []     #Current question list

        self.show_start_screen()    #Home screen

    #---Start Screen---
    def show_start_screen(self):
        self.clear_screen()         #Clear old widgets

        tk.Label(self.root, text="Quiz App", font=("Arial", 20, "bold", "underline"), 
                 bg="#f0f8ff").pack(pady=15) #Title

        tk.Label(self.root, text="Select Level", bg="#f0f8ff", fg="#111111").pack(pady=5)   #Level selection

        tk.Button(self.root, text="Easy", width=15, bg="#4CAF50", fg="#000000",
                  command=lambda: self.start_quiz("easy")).pack(pady=5)     #Easy level button

        tk.Button(self.root, text="Medium", width=15, bg="#FF9800", fg="#000000",
                  command=lambda: self.start_quiz("medium")).pack(pady=5)   #Medium level button

        tk.Button(self.root, text="Hard", width=15, bg="#f44336", fg="#000000",
                  command=lambda: self.start_quiz("hard")).pack(pady=5) #Hard level button

    #---Start Quiz---
    def start_quiz(self, level):    #Reset values
        self.score = 0
        self.q_index = 0
        self.questions = quiz_data[level][:]    #Copy questions for selected level
        random.shuffle(self.questions)  #Questions Shuffle randomly

        self.show_question()        #Show first question

    #---Show Question---
    def show_question(self):
        self.clear_screen()

        if self.q_index >= len(self.questions):         #Show result, if no more questions
            self.show_result()
            return

        q = self.questions[self.q_index]            #Current question

        tk.Label(self.root, text=f"Q{self.q_index + 1}: {q['question']}",
                 wraplength=300, font=("Arial", 12)).pack(pady=20)          #Display question

        for option in q["options"]:         #Button for each option
            tk.Button(self.root, text=option, width=20, bg="#21A6F3", fg="#fff",
                      command=lambda opt=option: self.check_answer(opt)).pack(pady=5)

    #---Check Answer---
    def check_answer(self, selected):
        correct = self.questions[self.q_index] ["answer"]           #Get Correct answer

        if selected == correct:
            self.score += 1         #increase score for correct answer

        self.q_index += 1           #Move to next question
        self.show_question()        #Show next question

    #---Result Screen---
    def show_result(self):
        self.clear_screen()

        total = len(self.questions)
        percentage = (self.score / total) * 100

        tk.Label(self.root, text="Result", font=("Arial", 20, "bold", "underline"), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text=f"Score: {self.score}/{total}", font=("Arial", 12), bg="#f0f8ff").pack()
        tk.Label(self.root, text=f"Percentage: {percentage:.2f}%", font=("Arial", 12), bg="#f0f8ff").pack()

        if percentage >= 80:            #performance message
            msg = "Excellent!"
        elif percentage >= 50:
            msg = "Good job!"
        else:
            msg = "Keep practicing!"

        tk.Label(self.root, text=msg, font=("Arial", 12, "bold"), bg="#f0f8ff").pack(pady=10)

        tk.Button(self.root, text="Play Again", bg="#9C27B0", fg="#fff", width=15,
                  command=self.show_start_screen).pack(pady=10)         #Restart quiz

    #---Clear Screen---
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="#f0f8ff")

#---Main loop---
root = tk.Tk()          # Create main window
app = QuizApp(root)     # Create app object
root.mainloop()         # run GUI loop