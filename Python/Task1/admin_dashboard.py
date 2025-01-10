"""
Description : Importing the Admin Functionalities and User Registration Functionalities 
"""
from question_paper import QuestionPaper, AnswerSets
from student import Login , SignUp ,StoringResult,student_access


def user_register():
    """
    Description : User Register function is used to check that the user is registered or not registered
                and if it is registered then it is admin or not

    Approach : Calling the login class default constructor to check the user input with the data stored in csv file return the username,password
    """
    isUser=input('Are you Already User ').lower().strip() == 'y' # Asking user is already registered or not
    if isUser:
        user=Login() # Calling the login class from the user registration module to login the user
        user_present,admin,username,password=user.verifying_credentials() # Verifying the Credential its username and password is in the csv file or not
        if user_present: 
            admin=admin[:-1]
            if admin=="True": # Verifying the user is admin or not 
                return 1,username,password   # If it is user as well as admin it return and provide the admin functionalities
            else:
                return 2,username,password   # If it is user but not admin it return and provide the student functionalities
        
        else:
            if password=="Invalid": # If User is providing invalid password
                return 3,None,None
            
    return 0,None,None

def admin_access():
    """
    Description : Admin Access function provides the functionalities of admin panel which creates the question paper answer sets 
                and add new user
    """
    task_to_perform=int(input("Enter 1 For adding new user\n2 For Creating Question Paper \n"))
    if task_to_perform==1: # Adding the New User / storing its data in the csv file
        SignUp() # Calling the SignUp class importing from User_registration file
    else: # Creating the question paper and its answer key set
        questions=QuestionPaper() # Creating the Object of Question paper set
        no_of_questions=questions.no_of_questions # Storing the number of questions user type
        answers_set=AnswerSets() # Creating the object of Answer Set
        answers_set.write_answer_sets(no_of_questions) # Calling the function write answer set to write the answer sets in the csv file



def main():
    """
    Description : Main Function is used to provided the access of the student dashboard and admin dashboard to the user and return if they are not registered
    """
    access_level,username,password=user_register() # Checking the user is exist or not and if exists user is admin or not
    if access_level==1:
        admin_access() # Providing The administrator authority
    elif access_level==2:
        score,total=student_access() # Providing the Student functionality
        StoringResult(score,total,username,password)
    elif access_level==3:
        return
    else:
        print("Please ask the administrator for registration.")
    

main() # Calling the main Function