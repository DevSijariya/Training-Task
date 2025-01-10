# Importing Regular Expression to used its functionalities to verify the username
import re

class SignUp:
    """
    Description : Creating the Sign Up Function and store in the csv file

    Approach : Creating the default constructor to take the input by the user when the user object is created
    """
    def __init__(self): # Creating the default constructor
        """
        Description : Creating the Default constructor which can call automatically when the object of the signup class is created 
                      
        Approach : It will take the username ,email , password from the user and stored the data in the csv file. 
<<<<<<< HEAD
                    
        """
=======
      
        """
        def valid_email():
            """
            Description : Used to varify the email is correct or not.

            Approach : It uses regular expression function to identify wheter the user input email is correct or not 
            """
            email=input("Enter Email id ") # Entering the user Email
            pattern = (r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$") # Predefined Pattern
            while re.match(pattern,email)==None: # Matching pattern with the user input email
                email=input("Please Enter a valid email") # Again taking the user input if the previous one is wrong
            return email # Returns the valid user email
        
>>>>>>> 2a439d4 ([Change] Optimise the Code)
        self.name=input("Enter UserName ") # Taking the User name input
        self.invalid_username = re.findall("[^a-zA-Z]",self.name)  # Validating the username is correct or not
        while self.invalid_username:
            self.name = input("Enter Valid UserName ")
            self.invalid_username = re.findall("[^a-zA-Z]",self.name)
        self.password=input("Enter Password ") # Taking the user password
<<<<<<< HEAD
        self.email=input("Enter Email id ") # Taking the 
        self.admin=input('Admin (y/n): ').lower().strip() == 'y'
        # import pdb;pdb.set_trace()
        # print(self.admin)
        self.storing_data_in_csv() # Calling the storing data csv function to store data in the csv file

=======
        self.email= valid_email() # Taking the valid user email by checking it

        self.admin=input('Admin (y/n): ').lower().strip() == 'y'
      
        self.storing_data_in_csv() # Calling the storing data csv function to store data in the csv file

   
>>>>>>> 2a439d4 ([Change] Optimise the Code)
    def storing_data_in_csv(user):
        """
        Description : This function is used to write the data of a user into csv file 

        Approach :  It open the csv file and append the data into it and if the csv file is not exists it will first create the file and then write the data 
                    After that it will close the csv file     
        
        Raise Exception :  File Exists Error can be occurs
        """
<<<<<<< HEAD
        try:
            UserInfo=open("UserInfo.csv",'x') # Checking the file is already exists or not
            UserInfo.write("Username , Password , Email Address, Admin \n") # Storing the Header for the file
        except:
            UserInfo=open("UserInfo.csv",'a') # opening file in the appending mode 

        UserInfo.write(f"{user.name},{user.password},{user.email},{user.admin}\n") # Appending the data in the csv file

        UserInfo.close() # Closing the CSV file
=======
        userinfo=open("userinfo.csv",'a+') # Opening the file in the read and append mode
        userinfo.seek(0)  # Move the pointer to the beginning
        userinfo.write(f"{user.name},{user.password},{user.email},{user.admin}\n") # Appending the data in the csv file
        userinfo.close() # Closing the CSV file
>>>>>>> 2a439d4 ([Change] Optimise the Code)



class Login:
    """
    Description : Creating a login Class which take the username and password and match if both are correct
                  It will give the access
    
    Approch : Creating Default Constructor which takes the username and password and send it to the Verifying Credential Function
              to verify the credentials and return result 
    """
<<<<<<< HEAD
    
=======

>>>>>>> 2a439d4 ([Change] Optimise the Code)
    def __init__(self):
        """
        Default Constructor which takes the username and password and Send it to the Verifying Credential Function For verifying

        Approach : It will take username and password and send it to the verifying credential function where the data is verify
        """
        self.username = input("Enter the Username ")
        self.password = input("Enter the Password ")

<<<<<<< HEAD
    def Verifying_Credentials(self):
        """
        Description : Verifying the User Credentials By Matching the user input with the user data which store in the csv file and returns
        """
        userinfo = open("UserInfo.csv",'r') # Opening the UserInfo csv file in the read mode
        userdata = userinfo.readlines() 
        userdata=[userdata[i].split(',') for i in range(len(userdata))] # Store the userdata in the list
        for data in range(len(userdata)):
            if userdata[data][0]==self.username and userdata[data][1]==self.password: # Checking the userinput data with the data store in the csv file if it match then login.
                # print(type(userdata[i][3]),userdata[i][3])
                return True,userdata[data][3],self.username,self.password # return the csv file
        for data in range(len(userdata)):
            if userdata[data][0]==self.username: # if username is match and password is not match then try 5 time if match then login else break
                number_of_try=4 # inititial number of trails
                while number_of_try:
                    password=input("Wrong Password. Please enter the correct password, ")
                    if password == userdata[data][1]: # checking the passwords
                        return True,userdata[data][3],self.username,self.password # return the data if password is correct
                    else:
                        number_of_try-=1
                print("Invalid Credentials")
                return False ,'False','False','Invalid'
        return False,'False','False','False' # Return false if the user failed to login
=======
    def verifying_credentials(self):
        """
        Description : Verifying the User Credentials By Matching the user input with the user data which store in the csv file and returns
        """
        userinfo = open("userinfo.csv",'a+') # Opening the UserInfo csv file in the read mode
        userinfo.seek(0)
        header = userinfo.readline()
        userdata = userinfo.readlines() 
        if header == '':
            userinfo.write(f"Username , Password , Email Address , Admin\n") 
            userinfo.write(f"dev,asdf,dev@gmail.com,True\n")
        number_of_users=len(userdata)
        userdata=[userdata[i].split(',') for i in range(number_of_users)] # Store the userdata in the list
        for data in range(number_of_users):
            if userdata[data][0]==self.username and userdata[data][1]==self.password: # Checking the userinput data with the data store in the csv file if it match then login.
                return True,userdata[data][3],self.username,self.password # return the csv file
        for data in range(number_of_users):
            if userdata[data][0]==self.username: # if username is match and password is not match then try 5 time if match then login else break
                number_of_try=4 # inititial number of trails
                while number_of_try: # Iterating the number of trails. 
                    password=input("Wrong Password. Please enter the correct password, ") # Taking the password 
                    if password == userdata[data][1]: # checking the passwords
                        return True,userdata[data][3],self.username,self.password # return the data if password is correct
                    else:
                        number_of_try-=1 # Decrement the number of trails if the password is wrong
                print("Invalid Credentials")
                return False ,False,False,'Invalid' # Return the false if number of trails is 0
        return False,False,False,False # Return false if the user failed to login
>>>>>>> 2a439d4 ([Change] Optimise the Code)
    
            
class StoringResult:
    """
    Description : Used to Create Result.csv file and store the students result in it

    Approach : Student Score is pass in this default constructors and the total marks 
               then this function calculates the percentage and store it in the csv file
<<<<<<< HEAD
=======

    Raise Exception : File Exists Exception is occurs if file is already created which can be handle by FileExistsError exception 
>>>>>>> 2a439d4 ([Change] Optimise the Code)
    """
    def __init__(self,score,total_marks,username,password):
        """
        Description : Default Constructor automatically call when student give exam to store their result
        """
        total_marks-=1
        percentage_score=(score/total_marks)*100 # Calculating the percentage of the students
        print(f"Your result is {percentage_score}")
<<<<<<< HEAD
        try:
            result=open("result.csv",'x') # Opening the csv file in the creating mode if file not exists
            result.write("Username,Password,Score \n") 
        except FileExistsError:
            result=open("result.csv",'a') # Opening the csv file in the append mode in the append mode
        result.write(f"{username},{password},{percentage_score}%\n") # Store the data in the result.csv file
=======
        result_file=open("result.csv",'a+') # Opening the csv file in the append mode in the append mode
        result_file.seek(0)
        number_of_lines=len(result_file.readlines()) # Counting the number of lines store in the csv file 
        # import pdb;pdb.set_trace()
        if number_of_lines == 0: # Checking the file containing headings or not
            result_file.write("Username,Password,Percentage\n")
        result_file.write(f"{username},{password},{percentage_score}%\n") # Store the data in the result.csv file
>>>>>>> 2a439d4 ([Change] Optimise the Code)



def student_access():
    """
    Description : Student access function provided the student to give Exam 
<<<<<<< HEAD
=======

    Approach : It Opens the questions.csv and answer.csv file in the read mode mode and display each questions which their corresponding options student have to 
               select one of the option if the option is correct it will add increase the score by 1 else score remains constant
               then it returns the students score to store it in result.csv file. 
>>>>>>> 2a439d4 ([Change] Optimise the Code)
    """
    print("Test Started \n") 
    score=0 # Initialize The Student Score with 0
    question_file = open("question_set.csv", 'r') # Opening the Question files to read the questions
    questions = question_file.readlines() # Reading Each lines in the question files
    answer_file = open("answers_set.csv",'r') # Opening the answers files to provide the Options of the particular question
    answers = answer_file.readlines() # Reading the answer files line by line
<<<<<<< HEAD
    count_split=0
    for ques in range(1,len(questions)): # Iterating the Questions and Answers line by line.
        print(questions[ques],end='')
        for ans in range(9,len(answers[ques])):
            if answers[ques][ans]=='[' or answers[ques][ans]==']': # Condition so that student unable to see the correct answer
                continue
            else:
                print(answers[ques][ans],end='')
=======
    for ques in range(1,len(questions)): # Iterating the Questions and Answers line by line.
        print(questions[ques],end='') # Printing the Questions in the console
        for ans in range(len(answers[ques])): 
            if answers[ques][ans]=='[' or answers[ques][ans]==']': # Condition so that student unable to see the correct answer
                continue
            else:
                print(answers[ques][ans],end='') # Printing the options in the console
>>>>>>> 2a439d4 ([Change] Optimise the Code)
            if (answers[ques][ans]==','):
                print("\t",end='') # Including the tab space 
        ans=answers[ques].split(',')
        while True:
            user_answer=input("Enter your Answer ").lower() # Taking user input for the answer
            if user_answer =='a' or user_answer=='b' or user_answer=='c' or user_answer=='d': # Checking that the user provide the valid option
                break
        if user_answer=='a' and ans[1][0]=='[': # Checking the user answers with the correct answers store in the csv file
            score+=1                            # Increment the student score if the answer provided by student is correct
        elif user_answer=='b' and ans[2][0]=='[':
            score+=1
        elif user_answer=='c' and ans[3][0]=='[':
            score+=1
        elif user_answer=='d' and ans[4][0]=='[':
            score+=1
    return score,len(questions) # Retturn the Score and the number of questions (Total Score)


