class QuestionPaper:
    """
    Description : Question Paper Class Used to Enter the Question in the csv file

    Approach : Take User input for number of questions , Then open the file (Create if not Exists) and then write the questions
               In the csv file
            
    Raise Exception : File Exists Error occurs when file is already created
    """
    def __init__(self): # Default Constructor to Enter the Number of Questions when The object is created
        self.no_of_questions =int(input("Enter the number of questions you Want to enter "))
        self.write_question() # Calling the write Function to write the data in the csv file
    def write_question(questions): #  This Function is used to Write the Question in the csv file
        f=open("question_set.csv",'w')
        f.write("S.no, Questions\n")
        for i in range(questions.no_of_questions):
            question=input(f"Question {i+1} : ") # Taking  user defined number of questions
            f.write(f"{i+1},{question}\n") # Writing questions when the file is not created
    
        f.close() # Closing the file


class AnswerSets:
    """
    Description : Answer Set Class Used to Enter the Answers key in the csv file
                  It Contain 4 options in which 1 is correct

    Approach : It uses number of questions to write the same numbers of answer set, 
               Then open the file (Create if not Exists) and then write the Answers set in 4 options In the csv file
            
    Raise Exception : File Exists Error occurs when file is already created
    """
    def write_answer_sets(answer,no_of_answer): # This Function is used to write the answer set in the csv file
        answer_number=1 # Assign a variable to track the answer number 
        question=open("question_set.csv",'r') # Opening the questions set file in the read mode
        questions_line=question.readlines()  # reading the each lines in the question File
        answers=open("answers_set.csv",'w') # Opening the answers
        answers.write("S.no, Option 1, Option 2, Option 3, Option 4\n") # writing the four options in the csv file
        while no_of_answer: # Iteration to store answers same as number of questions
            print("\n Question",questions_line[answer_number]) # Printing the single question at each iteration
            option1=input(f"Answer {answer_number} Option A: ")
            option2=input(f"Answer {answer_number} Option B: ")
            option3=input(f"Answer {answer_number} Option C: ")
            option4=input(f"Answer {answer_number} Option D: ")
            while True:
                correct_answer=input(f"Answer {answer_number} Correct Option is ").casefold() # Converting the Correct option in lower case so that it should be case insensitive
                if correct_answer=='a' or correct_answer=='b' or correct_answer=='c' or correct_answer=='d':
                    break   # Checking the correct option is valid or not
                else:
                    print("Invalid option Please retype the answer ")
            if correct_answer=='a':
                option1='['+option1+']' # Marking the correct options inside the brackets 
            elif correct_answer=='b':
                option2='['+option2+']'
            elif correct_answer=='c':
                option3='['+option3+']'
            else:
                option4='['+option4+']'    

            answers.write(f"Answer {answer_number},A {option1},B {option2},C {option3},D {option4}\n")
            no_of_answer-=1
            answer_number+=1
            

        answers.close() # Closing The File


# questions=QuestionPaper()
# questions.write_question()
# no_of_questions=questions.no_of_questions
# answers_set=AnswerSets()
# answers_set.write_answer_sets(no_of_questions)