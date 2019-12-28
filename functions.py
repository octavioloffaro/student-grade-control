# John Disandolo

import csv
from random import randint
from datetime import datetime
from tkinter import messagebox as msg

"""
CSV FUNCTIONS FILE
------------------
For reading and writing to csv data files.
Available to all windows.

"""


def find_test(testid) :
    """
    Used by other functions to find a particular test.

    This function shouldn't need to be used directly.
    Use the following few functions...

    """

    for count, row in enumerate(read_csv('data/tests.csv')) :
        
        if count != 0 : # skip header of CSV
            if int(row[0]) == testid :                
                return row

            
def is_valid_id(user_input) :
    """
    Check if given TestID exists.

    """
    
    try :
        if user_input == "" :
            raise Exception('Please enter a TestID first.\nYou should have received it by email.')

        if user_input.isdigit() == False :          # check user input is an int
            raise Exception('TestIDs should be a six-digit number.\nPlease try again.')

        if not(100000 <= int(user_input) <= 999999) :    
            raise Exception('TestIDs should be from 100,000 to 999,999.\nPlease try again.')
        
        if find_test(int(user_input)) == None :     # check test exists
            raise Exception('There is no test available for the TestID specified.\nPlease ensure it is correct.')

        # if test found
        return True        
            
    except Exception as e :
        msg.showerror("Error", "An error occurred:\n" + str(e))
        return False

        
def read_csv(filename) :
    """
    Used by other functions to read a given csv file.

    Available filenames:
    -  data/tests.csv
    -  data/lecturers.csv
    -  data/students.csv

    """

    try:
        with open(filename) as csvfile:
            rdr = csv.reader(csvfile)
            return list(rdr)

    except :
        msg.showerror("Error", "A critical error occurred while retrieving data.\nPlease try again.")
        

def get_test_questions(testid) :
    """
    Takes a test ID and returns a 2D list containing
    all questions with their respective answers.
    
    (testid is an integer from 100000 to 999999)


    Example output:
    [['Question 1 Title', 'Answer 1', '*Correct Answer'], ...]

    """

    test_info = find_test(testid)
    output = []
    
    if test_info != None :
        for question in test_info[3::2] :

            if question != "" :     # check for end of questions
                output += [[question]]
            else :
                break

        for count, answers in enumerate(test_info[4::2]) :

            if answers != "" :     # check for end of answers
                output[count] += answers.split('**')
            else :
                break

        return output
    
    else :
        msg.showerror("Error", "Test ID could not be found.")


def get_test_type(testid) :
    """
    Takes a test ID and returns a the type of that test
    (i.e. summative or formative).
    
    (testid is an integer from 100000 to 999999)


    Example output:
    'Summative'

    """

    test_info = find_test(testid)
    
    if test_info != None :
        return test_info[1]

    else :
        msg.showerror("Error", "Test ID could not be found.")


def get_test_deadline(testid) :
    """
    Takes a test ID and returns the test deadline.
    
    (testid is an integer from 100000 to 999999)


    Example output:
    'DD/MM/YYYY HH:MM' (in datetime format)

    """

    test_info = find_test(testid)
    
    if test_info != None :
        return datetime.strptime(test_info[2], '%d/%m/%Y %H:%M')

    else :
        msg.showerror("Error", "Test ID could not be found.")


def get_test_attempts(testid, studentid) :
    """
    Finds the number of attempts a student has taken
    on a specified test.
    
    (testid and studentid are integers from 100000 to 999999)


    Example output:
    3 (int)

    """

    attempts = 0
    
    try :
        with open('data/test' + str(testid) + '.csv') as csvfile:
            rdr = csv.reader(csvfile)
            
            for count, row in enumerate(rdr) :
            
                if count != 0 : # skip header of CSV
                    if int(row[0]) == studentid :
                        attempts += 1

        return attempts

    except :
        msg.showerror("Error", "Could not retrieve data.\nCheck that both the StudentID and TestID are correct.")
                          

def save_test(user_inputs) :
    """
    Takes lecturer's inputs for all questions (including
    their answers) and adds the data to a new csv file.

    user_inputs should be in the format (function assumes correct format):
    ['Summative', 'DD/MM/YYYY HH:MM', ["Question 1 Title", "Answer 1***Correct Answer"], ...]

    Answers for each question are separated by **
    with correct answers starting with one more *
    
    This function doesn't return anything.

    """

    id_exists = True
    testid = 0

    try :
        while id_exists :
            id_exists = False
            
            # generate random 6-digit testid
            testid = randint(100000, 999999)
                  
            for count, row in enumerate(read_csv('data/tests.csv')) :
                    
                if count != 0 : # skip header of CSV
                    if int(row[0]) == testid :                
                        id_exists = True
            
        
        # add type and deadline to list
        test_info = [testid] + user_inputs[0:2]

        for question in user_inputs[2:] :
            test_info += [question[0]]

            # trim extra asterisks off string and append
            trimmed = [question[1]][0].rstrip('*')
            test_info += [trimmed]


        # pad list if test has less than 10 questions
        test_info += [''] * (23 - len(test_info))


        # append test information to csv file
        with open('data/tests.csv', 'a', newline='') as csvfile : 
            writer = csv.writer(csvfile)
            writer.writerow(test_info)

        # create csv file ready for student responses
        with open('data/test' + str(testid) + '.csv', 'w', newline='') as csvfile : 
            writer = csv.writer(csvfile)
            writer.writerow(['StudentID', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

    except Exception as e:
        print(e)
        msg.showerror("Error", "A critical error occurred when saving the data.\nPlease try again.")


def save_response(testid, studentid, user_inputs) :
    """
    Takes student's response to a test and saves it
    into a relevant file.

    user_inputs should be in the format:
    [1,2,3,1,2,3,...]  --> i.e. number of answer chosen

    (testid and studentid are integers from 100000 to 999999)


    This function doesn't return anything.

    """

    try :
        with open('data/test' + str(testid) + '.csv', 'a', newline='') as csvfile : 
            writer = csv.writer(csvfile)
            writer.writerow([studentid] + user_inputs)

    except :
        msg.showerror("Error", "Could not save test answers.\nPlease try again.")
                      

def get_student_response(testid, studentid) :
    """
    Returns student's response to a particular test given
    the appropriate testid.
    
    (testid and studentid are integers from 100000 to 999999)


    Example output:
    [[1,2,3,1,2,3,...]]

    Multiple responses are given as:
    [[1,2,3,1,2,3,...], [1,2,3,1,2,3,...], ...]

    """

    responses = []
    try :
        with open('data/test' + str(testid) + '.csv') as csvfile:
            rdr = csv.reader(csvfile)
            
            for count, row in enumerate(rdr) :
            
                if count != 0 : # skip header of CSV
                    if int(row[0]) == studentid :

                        # return non-empty integer values
                        responses += [[int(x) for x in row[1:] if x]]

        return responses
    
    except :
        msg.showerror("Error", "Could not retrieve data.\nCheck that both the StudentID and TestID are correct.")


def get_correct_answers(testid) :
    """
    Returns list of correct answers.

    Example output:
    [1, 2, 3]
    
    """

    correct = []
    
    for question in get_test_questions(int(testid)) :
        for count, answer in enumerate(question[1:]) :
            if '*' in answer :
                correct += [count + 1]

    return correct
         
